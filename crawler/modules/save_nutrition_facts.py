import os

from .find_text_position_with_tesseract import find_text_position_with_tesseract
from .crop_image import crop_image


def save_nutrition_facts(dir_path):
    image_extensions = ["jpg", "jpeg", "png", "gif", "bmp"]

    for file_name in os.listdir(dir_path):
        if not file_name.split(".")[-1] in image_extensions:
            continue

        image_path = os.path.join(dir_path, file_name)
        search_targets = ["영양정보"]
        text_positions = find_text_position_with_tesseract(image_path, search_targets)

        for target in search_targets:
            if not text_positions[target]:
                continue

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
