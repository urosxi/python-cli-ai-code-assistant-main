from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads a file within the working directory and returns its text content, truncating it if longer than 10000 chars.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file to read the contents from, relative to the working directory. Required.",
            )
            # "working_directory": We won't allow the LLM to specify the `working_directory` argument. We'll hard code it.
        },
    ),
)


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            )
            # "working_directory": We won't allow the LLM to specify the `working_directory` argument. We'll hard code it.
        },
    ),
)


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a file within the working directory with the provided arguments and prints out its STDOUT and STDERR output.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="A .py file to execute, relative to the working directory. Required.",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="The list of strings representing command-line arguments passed to the file when executed. Optional.",
            ),
            # "working_directory": We won't allow the LLM to specify the `working_directory` argument. We'll hard code it.
        },
    ),
)


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes the given content to a file within the working directory. Creates the file if it doesn't exist and overwrites it if it does.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the target file, relative to the working directory. Required.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Text content to write to the file.",
            ),
            # "working_directory": We won't allow the LLM to specify the `working_directory` argument. We'll hard code it.
        },
    ),
)
