import io

import requests
import boto3


class CrawlerDataRegistrar:
    LOCAL_DOMAIN = "http://127.0.0.1:8000/"
    S3_DOMAIN = ""

    def register_food_category(self, data):
        return requests.post(f"{self.LOCAL_DOMAIN}/food/food-category", json=data)

    def register_product(self, data):
        return requests.post(f"{self.LOCAL_DOMAIN}/food/product", json=data)

    def register_nutrition(self, file_name, screenshot, data):
        self.upload_nutrition_facts_image(file_name, screenshot)

        return requests.post(f"{self.LOCAL_DOMAIN}/food/nutrition", json=data)

    def upload_nutrition_facts_image(self, file_name, screenshot):
        with io.BytesIO() as output:
            screenshot.save(output, format="PNG")
            output.seek(0)

            s3 = boto3.client("s3")
            s3.upload_fileobj(
                output,
                self.S3_DOMAIN,
                file_name,
                ExtraArgs={"ContentType": "image/png"},
            )
