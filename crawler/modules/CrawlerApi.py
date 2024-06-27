import requests


class CrawlerApi:
    BE_DOMAIN = "http://127.0.0.1:8000"

    def get_food_categories(self):
        return requests.get(f"{CrawlerApi.BE_DOMAIN}/food/food-category").json()

    def get_brands(self):
        return requests.get(f"{CrawlerApi.BE_DOMAIN}/food/brand").json()

    def register_food_category(self, category_key, category_name):
        return requests.post(
            url=f"{CrawlerApi.BE_DOMAIN}/food/food-category/",
            data={
                "category_key": category_key,
                "category_name": category_name,
            },
        ).json()

    def register_product(self, food_category, brand_name, product_name, coupang_url):
        return requests.post(
            url=f"{CrawlerApi.BE_DOMAIN}/food/product/",
            data={
                "food_categories": [food_category],
                "brand_name": brand_name,
                "product_name": product_name,
                "coupang_url": coupang_url,
            },
        ).json()

    def register_nutrition(self, product_id, data, s3_url):
        return requests.post(
            url=f"{CrawlerApi.BE_DOMAIN}/food/nutrition/",
            data={"product": product_id, "data": data, "s3_url": s3_url},
        ).json()
