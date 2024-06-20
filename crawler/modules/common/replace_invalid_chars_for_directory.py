import re


def replace_invalid_chars_for_directory(folder_name: str):
    cleaned_folder_name = re.sub(r'[<>:"/\\|?*]', "", folder_name)

    return cleaned_folder_name
