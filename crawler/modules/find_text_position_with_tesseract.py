from typing import List

import pytesseract
from PIL import Image

from . import constants


pytesseract.pytesseract.tesseract_cmd = constants.GOOGLE_TESSERACT_LOCATION


def find_text_position_with_tesseract(image_url: str, search_texts: List[str]):
    image = Image.open(image_url)
    alphabet_boxes = pytesseract.image_to_boxes(image, lang="kor")
    alphabet_lines = alphabet_boxes.splitlines()

    text_positions = {}

    for search_text in search_texts:
        current_text_positions = []

        for i in range(len(alphabet_lines)):
            line = alphabet_lines[i]
            alphabet = line.split(" ")[0]

            if alphabet == search_text[0]:
                searched_text = ""
                positions = []

                for line in alphabet_lines[i : i + len(search_text)]:
                    alphabet, left, bottom, right, top, _ = line.split(" ")

                    searched_text += alphabet
                    positions.append([left, bottom, right, top])

                if search_text == searched_text:
                    left_min = min(int(positions[0][0]), int(positions[-1][0]))
                    bottom_min = min(int(positions[0][1]), int(positions[-1][1]))
                    right_max = max(int(positions[0][2]), int(positions[-1][2]))
                    top_max = max(int(positions[0][3]), int(positions[-1][3]))

                    width, height = image.size

                    # top의 경우 위에서부터의 위치, bottom의 경우 아래에서부터 위치를 의미.
                    current_text_positions.append(
                        {
                            "top": height - top_max,
                            "bottom": bottom_min,
                            "left": left_min,
                            "right": width - right_max,
                        },
                    )

        text_positions[search_text] = current_text_positions

    return text_positions
