import os


def get_files_info(working_directory, directory="."):
    try:
        if directory.startswith("/") or directory.startswith(".."):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        full_path = os.path.abspath(
            os.path.join(os.getcwd(), working_directory, directory)
        )

        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'

        results = ""

        directory_contents = os.listdir(full_path)
        for item in directory_contents:
            item_path = os.path.join(full_path, item)
            item_desc = f"- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}\n"
            results += item_desc

        return results

    except Exception as e:
        return f"Error: {repr(e)}"


if __name__ == "__main__":
    print(get_files_info("calculator", "../"))
