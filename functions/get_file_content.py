import os
from config import *

def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    try:
        working_dir_abs_path = os.path.abspath(working_directory)
        full_abs_path = os.path.abspath(full_path)
        if not full_abs_path.startswith(working_dir_abs_path):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(full_abs_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(full_abs_path, "r") as f:
            raw_file = f.read()
            print(f"raw_file: {raw_file}")
            f.seek(0)
            if len(raw_file) > MAX_CHARS:
                file_content_string = f.read(MAX_CHARS)
                file_content_string = file_content_string + f'[...File "{full_abs_path}" truncated at {MAX_CHARS} characters]'
                return file_content_string
            else:
                return raw_file
    except Exception as e:
            return f'Error: "{e}"'
