import os

import pytesseract
from PIL import Image
from paddleocr import PaddleOCR

from . import constants
from .common import save_text_data


pytesseract.pytesseract.tesseract_cmd = constants.GOOGLE_TESSERACT_LOCATION


def save_all_texts_with_tesseract(dir_path: str):
    for file_name in os.listdir(dir_path):
        if not file_name.split(".")[-1] in constants.IMAGE_EXTENSIONS:
            continue

        image_path = os.path.join(dir_path, file_name)
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang="kor")

        save_text_data(
            save_dir=dir_path,
            file_name=f"all-text-data-{file_name}.txt",
            data=text,
            type="text",
        )


def save_all_texts_with_paddles(dir_path: str):
    for file_name in os.listdir(dir_path):
        if not file_name.split(".")[-1] in constants.IMAGE_EXTENSIONS:
            continue

        image_path = os.path.join(dir_path, file_name)

        paddle_ocr = PaddleOCR(lang="korean", use_angle_cls=False)
        result = paddle_ocr.ocr(image_path, cls=False)
        ocr_result = result[0]

        save_text_data(
            save_dir=dir_path,
            file_name=f"all-text-data-{file_name}.json",
            data={"ocr_result": ocr_result},
            type="json",
        )
