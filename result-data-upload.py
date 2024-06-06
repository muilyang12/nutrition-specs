import csv
import requests

with open("result-data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)

    enrolled_category_key = set()

    for line in reader:
        category_key, category_name, brand_name, product_name, coupang_url = line[:5]

        if not category_key in enrolled_category_key:
            enrolled_category_key.add(category_key)

            requests.post(
                url="http://127.0.0.1:8000/food/food-category/",
                data={
                    "category_key": category_key,
                    "category_name": category_name,
                },
            )
