from PIL import Image


def preprocess_image(image: Image.Image, threshold: int = 128) -> Image.Image:
    image = image.convert("L")

    if threshold > 255 or threshold < 0:
        return image.point(lambda x: 0 if x < 128 else 255, "1")

    return image.point(lambda x: 0 if x < threshold else 255, "1")
