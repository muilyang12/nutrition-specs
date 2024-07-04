import requests
import io

import boto3


class CrawlerApi:
    BE_DOMAIN = "http://127.0.0.1:8000"

    BUCKET_NAME = "muilyang12-nutriinsights"
    S3_DOMAIN = ""

    def __init__(self):
        self.s3_client = boto3.client("s3")

    def get_food_categories(self):
        return requests.get(f"{CrawlerApi.BE_DOMAIN}/food/food-category").json()

    def get_brands(self, category_id):
        return requests.get(
            f"{CrawlerApi.BE_DOMAIN}/food/brand?food-category={category_id}"
        ).json()

    def register_food_category(self, category_key, category_name, parent_category):
        return requests.post(
            url=f"{CrawlerApi.BE_DOMAIN}/food/food-category/",
            data={
                "category_key": category_key,
                "category_name": category_name,
                "parent_category": parent_category,
            },
        ).json()

    def register_brand(self, category_ids, brand_name):
        return requests.post(
            url=f"{CrawlerApi.BE_DOMAIN}/food/brand/",
            data={
                "food_categories": category_ids,
                "name": brand_name,
            },
        ).json()

    def register_product(self, food_categories, brand, product_name, coupang_url):
        return requests.post(
            url=f"{CrawlerApi.BE_DOMAIN}/food/product/",
            data={
                "food_categories": food_categories,
                "brand": brand,
                "product_name": product_name,
                "coupang_url": coupang_url,
            },
        ).json()

    def register_nutrition(self, product_id, data, s3_key):
        return requests.post(
            url=f"{CrawlerApi.BE_DOMAIN}/food/nutrition/",
            data={"product": product_id, "data": data, "s3_key": s3_key},
        ).json()

    def upload_nutrition_facts_image(self, s3_key, screenshot):
        with io.BytesIO() as output:
            screenshot.save(output, format="PNG")
            output.seek(0)

            self.s3_client.put_object(
                Bucket=self.BUCKET_NAME,
                Key=s3_key,
                Body=output,
                ContentType="image/png",
            )
