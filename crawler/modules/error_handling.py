import os

import pytesseract
from PIL import Image

from . import constants
from .save_text_data import save_text_data


pytesseract.pytesseract.tesseract_cmd = constants.GOOGLE_TESSERACT_LOCATION


def save_all_texts_with_tesseract(dir_path: str):
    for file_name in os.listdir(dir_path):
        if not file_name.split(".")[-1] in constants.IMAGE_EXTENSIONS:
            continue

        image = Image.open(f"{dir_path}/{file_name}")
        text = pytesseract.image_to_string(image, lang="kor")

        save_text_data(
            save_dir=dir_path,
            file_name=f"all-text-data-{file_name}.txt",
            data=text,
            type="text",
        )
