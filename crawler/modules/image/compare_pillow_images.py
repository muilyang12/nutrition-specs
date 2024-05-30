from typing import List, Dict

from PIL import Image
import matplotlib.pyplot as plt


def compare_pillow_images(images: List[Dict[Image.Image, str]]) -> None:
    if not isinstance(images, list):
        raise ValueError("images must be a list of dictionaries")

    num_image = len(images)

    _, axs = plt.subplots(1, num_image, figsize=(5 * num_image, 5))

    for ax, img_dict in zip(axs, images):
        if not isinstance(img_dict, dict):
            raise ValueError("Each item in images must be a dictionary")
        if "image" not in img_dict or "title" not in img_dict:
            raise ValueError("Each dictionary must contain 'image' and 'title' keys")
        if not isinstance(img_dict["image"], Image.Image):
            raise ValueError("'image' must be a PIL Image object")
        if not isinstance(img_dict["title"], str):
            raise ValueError("'title' must be a string")

        image = img_dict["image"]
        title = img_dict["title"]

        ax.imshow(image)
        ax.set_title(title)
        ax.axis("off")

    plt.show()
