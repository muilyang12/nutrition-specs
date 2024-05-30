from typing import List

import pytesseract
from PIL import Image, ImageFilter, ImageEnhance
import cv2

import matplotlib.pyplot as plt

from . import constants


pytesseract.pytesseract.tesseract_cmd = constants.GOOGLE_TESSERACT_LOCATION


# def preprocess_image1(image: Image.Image) -> Image.Image:
#     # 그레이스케일 변환
#     image = image.convert("L")
#     # 이진화
#     image_binary = image.point(lambda x: 0 if x < 180 else 255, "1")

#     image88 = image.point(lambda x: 0 if x < 88 else 255, "1")
#     image128 = image.point(lambda x: 0 if x < 128 else 255, "1")
#     image168 = image.point(lambda x: 0 if x < 168 else 255, "1")

#     # 이미지를 표시하기 위해 서브플롯 생성
#     fig, axs = plt.subplots(1, 3, figsize=(15, 5))

#     # 첫 번째 이미지
#     axs[0].imshow(image88)
#     axs[0].set_title("image88")
#     axs[0].axis("off")

#     # 두 번째 이미지
#     axs[1].imshow(image128)
#     axs[1].set_title("image128")
#     axs[1].axis("off")

#     # 두 번째 이미지
#     axs[2].imshow(image168)
#     axs[2].set_title("image168")
#     axs[2].axis("off")

#     # 이미지 보여주기
#     plt.show()

#     return image168


# def preprocess_image2(image_path: str) -> Image.Image:
#     # OpenCV로 이미지 읽기
#     image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

#     # # 이미지 확대
#     # image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

#     # # GaussianBlur로 노이즈 제거
#     # image = cv2.GaussianBlur(image, (5, 5), 0)

#     # Otsu 이진화
#     _, image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

#     # OpenCV 이미지를 PIL 이미지로 변환
#     pil_image = Image.fromarray(image)

#     return pil_image


def preprocess_image(image_path: str) -> Image.Image:
    # 이미지 읽기
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 이미지 확대
    gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # GaussianBlur로 노이즈 제거
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Otsu 이진화
    _, binary_image = cv2.threshold(
        blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    # 여백 제거
    coords = cv2.findNonZero(binary_image)
    x, y, w, h = cv2.boundingRect(coords)
    rect = binary_image[y : y + h, x : x + w]

    # PIL 이미지로 변환
    pil_image = Image.fromarray(rect)

    # 밝기와 대비 향상
    enhancer = ImageEnhance.Contrast(pil_image)
    enhanced_image = enhancer.enhance(2)
    enhancer = ImageEnhance.Brightness(enhanced_image)
    final_image = enhancer.enhance(1.5)

    return final_image


def find_text_position_with_tesseract(image_path: str, search_texts: List[str]):
    image = Image.open(image_path)

    # preprocess_image.preprocess_image(image=image, compare=[50, 100, 150, 200])
    aaa = preprocess_image(image_path)

    aaa.show()

    alphabet_boxes = pytesseract.image_to_boxes(image, lang="kor")
    alphabet_lines = alphabet_boxes.splitlines()

    print(alphabet_lines)

    text_positions = {}

    for search_text in search_texts:
        current_text_positions = []

        for i in range(len(alphabet_lines)):
            line = alphabet_lines[i]
            alphabet = line.split(" ")[0]

            if alphabet != search_text[0]:
                continue

            searched_text = ""
            positions = []

            for line in alphabet_lines[i : i + len(search_text)]:
                alphabet, left, bottom, right, top, _ = line.split(" ")

                searched_text += alphabet
                positions.append([left, bottom, right, top])

            if search_text != searched_text:
                continue

            left_min = min(int(positions[0][0]), int(positions[-1][0]))
            bottom_min = min(int(positions[0][1]), int(positions[-1][1]))
            right_max = max(int(positions[0][2]), int(positions[-1][2]))
            top_max = max(int(positions[0][3]), int(positions[-1][3]))

            width, height = image.size

            # top의 경우 위에서부터의 위치, bottom의 경우 아래에서부터 위치를 의미.
            current_text_positions.append(
                {
                    "top": height - top_max,
                    "bottom": bottom_min,
                    "left": left_min,
                    "right": width - right_max,
                },
            )

        text_positions[search_text] = current_text_positions

    return text_positions
