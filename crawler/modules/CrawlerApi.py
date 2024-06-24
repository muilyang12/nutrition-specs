import requests


class CrawlerApi:
    BE_DOMAIN = "http://127.0.0.1:8000"

    def get_food_categories(self):
        return requests.get(f"{CrawlerApi.BE_DOMAIN}/food/food-category").json()

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
                "food_category": food_category,
                "brand_name": brand_name,
                "product_name": product_name,
                "coupang_url": coupang_url,
            },
        ).json()
