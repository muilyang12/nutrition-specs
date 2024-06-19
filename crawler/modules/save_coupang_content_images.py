import os
from io import BytesIO
from PIL import Image

from .coupang_api import coupang_get_with_headers


def save_coupang_content_images(save_dir: str, details):
    os.makedirs(save_dir, exist_ok=True)

    index = 0

    for item in details:
        if item["contentType"] == "IMAGE_NO_SPACE":
            index += 1

            for description in item["vendorItemContentDescriptions"]:
                image_url = "https:" + description["content"]
                image_extension = image_url.split("/")[-1].split(".")[-1]

                response = coupang_get_with_headers(image_url)
                image_data = response.content

                if len(image_data) < 2 * 1024 * 1024:
                    image_name = f"{index}.{image_extension}"
                    image_path = os.path.join(save_dir, image_name)

                    with open(image_path, "wb") as file:
                        file.write(image_data)

                else:
                    image = Image.open(BytesIO(image_data))
                    width, height = image.size

                    half_height = height // 2
                    upper_half = image.crop((0, 0, width, half_height))
                    lower_half = image.crop((0, half_height, width, height))

                    image_path1 = os.path.join(save_dir, f"{index}-1.{image_extension}")
                    image_path2 = os.path.join(save_dir, f"{index}-2.{image_extension}")

                    upper_half.save(image_path1)
                    lower_half.save(image_path2)

        else:
            file_path = os.path.join(save_dir, "weird_content_type.txt")

            with open(file_path, "a", encoding="utf-8") as file:
                file.write(str(item["contentType"]))
