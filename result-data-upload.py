import csv
import requests
from collections import defaultdict

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
                "food-category": enrolled_categories[category_key],
                "brand_name": brand_name,
                "product_name": product_name,
                "coupang_url": coupang_url,
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
                "serving_size": serving_size,
                "serving_unit": serving_unit,
                "calories": calories,
                "total_carbohydrate": total_carbohydrate,
                "sugars": sugars,
                "sugar_alcohols": sugar_alcohols,
                "dietary_fiber": dietary_fiber,
                "allulose": allulose,
                "total_fat": total_fat,
                "saturated_fat": saturated_fat,
                "trans_fat": trans_fat,
                "cholesterol": cholesterol,
                "protein": protein,
                "sodium": sodium,
                "calcium": calcium,
            },
        )
