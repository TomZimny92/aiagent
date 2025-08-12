import os
from pathlib import Path
from config import *

def write_file(working_directory, file_path, content):
    
    try:
        while file_path.startswith('/') or file_path.startswith('.'):
            file_path = file_path[1:]
        full_path = os.path.join(working_directory, file_path)
        working_dir_abs_path = os.path.abspath(working_directory)
        #print(f"working_dir_abs_path: {working_dir_abs_path}")
        #file_abs_path = os.path.abspath(file_path)
        full_abs_path = os.path.abspath(full_path)
        #print(f"full_abs_path: {full_abs_path}")
        #print(f"workdirabs: {working_dir_abs_path}")
        #print(f"file_abs_path: {file_abs_path}")
        fp = Path(full_abs_path)
        print(f"fp.name: {fp.name}")
        print(f"fp.parent: {fp.parent}")
        #print(f"commonpath: {os.path.commonpath([full_abs_path, working_dir_abs_path])}")
        if os.path.commonpath([full_abs_path, working_dir_abs_path]) != working_dir_abs_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(fp.parent):
            os.makedirs(fp.parent)
        with open(fp.name, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: "{e}"'
