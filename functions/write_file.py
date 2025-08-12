import os
from config import *

def write_file(working_directory, file_path, content):
    full_path = os.path.join(working_directory, file_path)
    try:
        working_dir_abs_path = os.path.abspath(working_directory)
        full_abs_path = os.path.abspath(full_path)
        if not full_abs_path.startswith(working_dir_abs_path):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        with open(file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: "{e}"'
