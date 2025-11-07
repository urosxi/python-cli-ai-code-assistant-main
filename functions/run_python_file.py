import os
import subprocess


def run_python_file(working_directory, file_path, args=[]):
    try:
        if file_path.startswith("/") or file_path.startswith(".."):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        full_path = os.path.abspath(
            os.path.join(os.getcwd(), working_directory, file_path)
        )

        if not os.path.isfile(full_path):
            return f'Error: File "{file_path}" not found.'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        completed_process = subprocess.run(
            ["python3", full_path, *args],
            text=True,
            capture_output=True,
            timeout=30,
        )

        has_process_error = completed_process.returncode != 0
        if has_process_error:
            print("Process exited with code ", completed_process.returncode)

        if not completed_process.stdout:
            return "No output produced."

    except Exception as e:
        f"Error: executing Python file: {e}"
