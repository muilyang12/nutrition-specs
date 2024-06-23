import io
import csv

import requests
import boto3


class CrawlerDataRegistrarTool:
    LOCAL_DOMAIN = "http://127.0.0.1:8000/"
    S3_DOMAIN = ""

    def __init__(self, app):
        self.app = app

    def register_data(self):
        values = self.app.selected_product_values
        row = [
            values[self.app.ui.column_index["category_key"]],
            values[self.app.ui.column_index["category_name"]],
            values[self.app.ui.column_index["brand_name"]],
            values[self.app.ui.column_index["product_name"]],
            values[self.app.ui.column_index["url"]],
        ]

        with open("../result-data.csv", mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(row)

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
