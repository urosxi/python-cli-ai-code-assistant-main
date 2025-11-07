import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import MAX_ITERATIONS
from prompts import system_prompt
from functions.schemas import (
    schema_get_file_content,
    schema_get_files_info,
    schema_run_python_file,
    schema_write_file,
)
from functions.call_function import call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

model_name = "gemini-2.0-flash-001"


available_functions = types.Tool(
    function_declarations=[
        schema_get_file_content,
        schema_get_files_info,
        schema_run_python_file,
        schema_write_file,
    ]
)


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model=model_name,
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )

    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    if response.candidates:
        for item in response.candidates:
            messages.append(item.content)

    if not response.function_calls:
        return response.text

    function_responses = []
    if response.function_calls:
        for func_call_info in response.function_calls:
            tool_response = call_function(func_call_info)
            tool_response_part = tool_response.parts[0]

            function_responses.append(tool_response_part)

            if verbose:
                print(f"-> {tool_response_part.function_response.response}")

    messages.append(types.Content(role="user", parts=function_responses))


def main():
    verbose_mode = "--verbose" in sys.argv
    args = []

    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("AI Bot")
        print("\nUsage: python main.py <user prompt> [--verbose]")
        print('Example: python main.py "How do I fix the error in tests.py?"')
        sys.exit(1)

    user_prompt = " ".join(args)

    if verbose_mode:
        print(f"User prompt: {user_prompt}\n")

    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

    # Agent feedback loop - call LLM repeatedly at most 20 times
    for _ in range(MAX_ITERATIONS):
        try:
            final_response = generate_content(client, messages, verbose_mode)
            if final_response:
                print("Final response:")
                print(final_response)
                break

        except Exception as e:
            print(f"Error in generate_content: {e}")


if __name__ == "__main__":
    main()
