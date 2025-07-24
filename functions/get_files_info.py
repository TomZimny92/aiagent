import os

def get_files_info(working_directory, directory="."):
    full_path = os.path.join(working_directory, directory)
    try:
        working_dir_abs_path = os.path.abspath(working_directory)
        full_abs_path = os.path.abspath(full_path)
        if not full_abs_path.startswith(working_dir_abs_path):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(full_abs_path):
            return f'Error: "{directory}" is not a directory'
        filenames = os.listdir(full_abs_path)
        print_files = []
        for file in filenames:
            file_path = os.path.join(full_abs_path, file)
            file_size = os.path.getsize(file_path)
            is_file_dir = os.path.isdir(file_path)
            result = f"- {file}: file_size={file_size} bytes, is_dir={is_file_dir}"
            print_files.append(result)
        final_result = "\n".join(print_files)
        return final_result
    except Exception as e:
        return f'Error: "{e}"'
