import re
import os


def replace_invalid_chars_for_directory(folder_name: str):
    cleaned_folder_name = re.sub(r'[<>:"/\\|?*]', "", folder_name)

    return cleaned_folder_name


def get_path(*args):
    components = [replace_invalid_chars_for_directory(arg) for arg in args]

    return os.path.join(*components)
