from PIL import Image
import cv2 as cv
import numpy as np


def get_preprocessed_image1(image_path: str, threshold: int = 128) -> Image.Image:
    image = Image.open(image_path)
    gray_image = image.convert("L")

    if threshold > 255 or threshold < 0:
        return gray_image.point(lambda x: 0 if x < 128 else 255, "1")

    return gray_image.point(lambda x: 0 if x < threshold else 255, "1")


# OpenCV Image Thresholding
# https://docs.opencv.org/4.6.0/d7/d4d/tutorial_py_thresholding.html
def get_preprocessed_image2(image_path: str) -> None:
    image = cv.imread(image_path)
    cv.imshow("Original", image)

    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Simple Thresholding
    _, simple_thresh_image1 = cv.threshold(gray_image, 107, 255, cv.THRESH_BINARY)
    _, simple_thresh_image2 = cv.threshold(gray_image, 127, 255, cv.THRESH_BINARY)
    _, simple_thresh_image3 = cv.threshold(gray_image, 147, 255, cv.THRESH_BINARY)

    cv.imshow("Simple Thresholding - Threshold 107", simple_thresh_image1)
    cv.imshow("Simple Thresholding - Threshold 127", simple_thresh_image2)
    cv.imshow("Simple Thresholding - Threshold 147", simple_thresh_image3)

    # Otsu's Binarization
    _, otsu_thresh_image = cv.threshold(
        gray_image, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU
    )

    cv.imshow("Otsu's Binarization", otsu_thresh_image)

    # Adaptive Thresholding
    # The algorithm determines the threshold for a pixel based on a small region around it.
    # If an image has different lighting conditions in different areas
    adaptive_thresh_image1 = cv.adaptiveThreshold(
        gray_image, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2
    )
    adaptive_thresh_image2 = cv.adaptiveThreshold(
        gray_image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2
    )

    cv.imshow("Adaptive Thresholding - MEAN", adaptive_thresh_image1)
    cv.imshow("Adaptive Thresholding - GAUSSIAN", adaptive_thresh_image2)

    cv.waitKey(0)


# OpenCV Morphological Transformations
# https://docs.opencv.org/4.6.0/d9/d61/tutorial_py_morphological_ops.html
def get_preprocessed_image3(image_path: str) -> None:
    image = cv.imread(image_path)
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("Original - Grayscale", gray_image)

    # Erosion
    kernel = np.ones((3, 3), np.uint8)
    erosion_image = cv.erode(gray_image, kernel, iterations=1)
    cv.imshow("Erosion", erosion_image)

    # Dilation
    kernel = np.ones((3, 3), np.uint8)
    dilation_image = cv.dilate(gray_image, kernel, iterations=1)
    cv.imshow("Dilation", dilation_image)

    # Opening
    opening_image = cv.morphologyEx(gray_image, cv.MORPH_OPEN, kernel)
    cv.imshow("Opening", opening_image)

    # Closing
    closing_image = cv.morphologyEx(gray_image, cv.MORPH_CLOSE, kernel)
    cv.imshow("Closing", closing_image)

    cv.waitKey(0)
