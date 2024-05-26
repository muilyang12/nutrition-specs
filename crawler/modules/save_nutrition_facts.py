import os

from PIL import Image


# top의 경우 위에서부터의 위치, bottom의 경우 아래에서부터 위치를 의미.
def save_nutrition_facts(image_path: str, new_file_name: str, top, bottom, left, right):
    image = Image.open(image_path)

    width, height = image.size

    crop_box = (left, top, width - right, height - bottom)
    cropped_image = image.crop(crop_box)

    directory, _ = os.path.split(image_path)

    new_directory = os.path.join(directory, "nutrition-facts")
    os.makedirs(new_directory, exist_ok=True)
    save_path = os.path.join(new_directory, new_file_name)

    cropped_image.save(save_path)
