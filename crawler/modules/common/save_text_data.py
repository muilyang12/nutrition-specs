import os
import json


def save_text_data(save_dir: str, file_name: str, data, type: str = "json"):
    os.makedirs(save_dir, exist_ok=True)

    file_path = os.path.join(save_dir, file_name)

    with open(file_path, "w", encoding="utf-8") as file:
        if type == "json":
            json.dump(data, file, ensure_ascii=False, indent=4)
        else:
            file.write(str(data))
