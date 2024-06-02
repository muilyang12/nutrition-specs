import os

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
                image_name = f"{index}.{image_extension}"
                image_path = os.path.join(save_dir, image_name)

                response = coupang_get_with_headers(image_url)
                with open(image_path, "wb") as file:
                    file.write(response.content)

        else:
            file_path = os.path.join(save_dir, "weird_content_type.txt")

            with open(file_path, "a", encoding="utf-8") as file:
                file.write(str(item["contentType"]))
