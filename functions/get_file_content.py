import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    try:
        if file_path.startswith("/") or file_path.startswith(".."):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        full_path = os.path.abspath(
            os.path.join(os.getcwd(), working_directory, file_path)
        )

        if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(full_path, mode="r") as f:
            file_content = f.read(MAX_CHARS)
            has_more_content = len(f.read(10)) > 0

            if has_more_content:
                file_content += f'[...File "{file_path}" truncated at 10000'

        return file_content

    except Exception as e:
        return f"Error: {e}"
