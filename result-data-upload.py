import csv
import requests
from collections import defaultdict


def get_value(value):
    return value if value != "-" else None


with open("result-data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)

    enrolled_categories = defaultdict(int)

    for line in reader:
        category_key, category_name, brand_name, product_name, coupang_url = line[:5]

        if not category_key in enrolled_categories:
            category_res = requests.post(
                url="http://127.0.0.1:8000/food/food-category/",
                data={
                    "category_key": category_key,
                    "category_name": category_name,
                },
            ).json()

            enrolled_categories[category_key] = category_res["id"]

        product_res = requests.post(
            url="http://127.0.0.1:8000/food/product/",
            data={
                "food_category": enrolled_categories[category_key],
                "brand_name": brand_name,
                "product_name": product_name,
                "coupang_url": get_value(coupang_url),
            },
        ).json()

        product_id = product_res["id"]

        (
            serving_size,
            serving_unit,
            calories,
            total_carbohydrate,
            sugars,
            sugar_alcohols,
            dietary_fiber,
            allulose,
            total_fat,
            saturated_fat,
            trans_fat,
            cholesterol,
            protein,
            sodium,
            calcium,
        ) = line[5:]

        requests.post(
            url="http://127.0.0.1:8000/food/nutrition/",
            data={
                "product": product_id,
                "serving_size": get_value(serving_size),
                "serving_unit": get_value(serving_unit),
                "calories": get_value(calories),
                "total_carbohydrate": get_value(total_carbohydrate),
                "sugars": get_value(sugars),
                "sugar_alcohols": get_value(sugar_alcohols),
                "dietary_fiber": get_value(dietary_fiber),
                "allulose": get_value(allulose),
                "total_fat": get_value(total_fat),
                "saturated_fat": get_value(saturated_fat),
                "trans_fat": get_value(trans_fat),
                "cholesterol": get_value(cholesterol),
                "protein": get_value(protein),
                "sodium": get_value(sodium),
                "calcium": get_value(calcium),
            },
        )
