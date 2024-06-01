from typing import List

from paddleocr import PaddleOCR
from PIL import Image


def find_text_position_with_paddle(image_path: str, search_texts: List[str]):
    text_positions = {}

    for text in search_texts:
        text_positions[text] = []

    paddle_ocr = PaddleOCR(lang="korean", use_angle_cls=False)
    result = paddle_ocr.ocr(image_path, cls=False)
    ocr_result = result[0]

    for word_info in ocr_result:
        position = word_info[0]
        text, _ = word_info[1]

        if not text in search_texts:
            continue

        image = Image.open(image_path)
        width, height = image.size

        left_top, right_top, right_bottom, left_bottom = position

        print(text, left_top, right_top, right_bottom, left_bottom)

        # top의 경우 위에서부터의 위치, bottom의 경우 아래에서부터 위치를 의미.
        text_positions[text].append(
            {
                "top": min(left_top[1], right_top[1]),
                "bottom": height - max(left_bottom[1], right_bottom[1]),
                "left": min(left_top[0], left_bottom[0]),
                "right": width - max(right_top[0], right_bottom[0]),
            },
        )

    return text_positions
