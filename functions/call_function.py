from google.genai import types
from config import WORKING_DIR
from .get_file_content import get_file_content
from .get_files_info import get_files_info
from .run_python_file import run_python_file
from .write_file import write_file

functions_map = {
    "get_file_content": get_file_content,
    "get_files_info": get_files_info,
    "run_python_file": run_python_file,
    "write_file": write_file,
}


def call_function(function_call_part, verbose=False):
    fn_name, fn_args = function_call_part.name, function_call_part.args

    if verbose:
        print(f"Calling function: {fn_name}({fn_args})")
    else:
        print(f" - Calling function: {fn_name}")

    kwargs = dict(fn_args)
    kwargs["working_directory"] = WORKING_DIR

    fn = functions_map.get(fn_name, None)

    if not fn:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=fn_name,
                    response={"error": f"Unknown function: {fn_name}"},
                )
            ],
        )

    fn_result = fn(**kwargs)

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=fn_name, response={"result": fn_result}
            )
        ],
    )
