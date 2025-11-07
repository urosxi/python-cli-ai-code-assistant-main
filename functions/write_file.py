import os


def write_file(working_directory, file_path, content):
    try:
        if file_path.startswith("/") or file_path.startswith(".."):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        full_path = os.path.abspath(
            os.path.join(os.getcwd(), working_directory, file_path)
        )

        with open(full_path, "w") as f:
            f.write(content)

        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as e:
        print(f"Error: {e}")
