import os

from . import constants
from .find_text_position_with_tesseract import find_text_position_with_tesseract
from .crop_image import crop_image
from .error_handling import save_all_texts_with_tesseract


def save_nutrition_facts(dir_path):
    save_count_per_dir = 0

    for file_name in os.listdir(dir_path):
        if not file_name.split(".")[-1] in constants.IMAGE_EXTENSIONS:
            continue

        image_path = os.path.join(dir_path, file_name)
        search_targets = ["영양정보"]
        text_positions = find_text_position_with_tesseract(image_path, search_targets)

        for target in search_targets:
            if not text_positions[target]:
                continue

            save_count_per_dir += 1

            positions = text_positions[target]

            for position in positions:
                left, top, right, bottom = (
                    position["left"],
                    position["top"],
                    position["right"],
                    position["bottom"],
                )

                crop_image(
                    image_path=f"{dir_path}/{file_name}",
                    save_as="nutrition-facts.jpg",
                    top=top - 50,
                    bottom=bottom - 300,
                    left=0,
                    right=0,
                )

    print(f"{save_count_per_dir} tables were found in the directory '{dir_path}'.")

    # 영양 데이터를 하나도 못 찾은 경우
    if save_count_per_dir == 0:
        save_all_texts_with_tesseract(dir_path)
