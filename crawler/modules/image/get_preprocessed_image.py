from PIL import Image


def get_preprocessed_image(image_path: str, threshold: int = 128) -> Image.Image:
    image = Image.open(image_path)
    gray_image = image.convert("L")

    if threshold > 255 or threshold < 0:
        return gray_image.point(lambda x: 0 if x < 128 else 255, "1")

    return gray_image.point(lambda x: 0 if x < threshold else 255, "1")
