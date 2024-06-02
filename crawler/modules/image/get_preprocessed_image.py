from PIL import Image
import cv2


def get_preprocessed_image1(image_path: str, threshold: int = 128) -> Image.Image:
    image = Image.open(image_path)
    gray_image = image.convert("L")

    if threshold > 255 or threshold < 0:
        return gray_image.point(lambda x: 0 if x < 128 else 255, "1")

    return gray_image.point(lambda x: 0 if x < threshold else 255, "1")


# OpenCV Image Thresholding
# https://docs.opencv.org/4.6.0/d7/d4d/tutorial_py_thresholding.html
def get_preprocessed_image2(image_path: str) -> None:
    image = cv2.imread(image_path)
    cv2.imshow("Original", image)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Simple Thresholding
    _, simple_thresh_image1 = cv2.threshold(gray_image, 107, 255, cv2.THRESH_BINARY)
    _, simple_thresh_image2 = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    _, simple_thresh_image3 = cv2.threshold(gray_image, 147, 255, cv2.THRESH_BINARY)

    cv2.imshow("Simple Thresholding - Threshold 107", simple_thresh_image1)
    cv2.imshow("Simple Thresholding - Threshold 127", simple_thresh_image1)
    cv2.imshow("Simple Thresholding - Threshold 147", simple_thresh_image1)

    # Otsu's Binarization
    _, otsu_thresh_image = cv2.threshold(
        gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    cv2.imshow("Otsu's Binarization", otsu_thresh_image)

    # Adaptive Thresholding
    # The algorithm determines the threshold for a pixel based on a small region around it.
    # If an image has different lighting conditions in different areas
    adaptive_thresh_image1 = cv2.adaptiveThreshold(
        gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
    )
    adaptive_thresh_image2 = cv2.adaptiveThreshold(
        gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )

    cv2.imshow("Adaptive Thresholding - MEAN", adaptive_thresh_image1)
    cv2.imshow("Adaptive Thresholding - GAUSSIAN", adaptive_thresh_image2)

    cv2.waitKey(0)
