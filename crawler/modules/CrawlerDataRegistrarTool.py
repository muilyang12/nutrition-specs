import io
import csv

import boto3
from pynput import keyboard
import win32clipboard

from .CrawlerApi import CrawlerApi
from .common import get_path


class CrawlerDataRegistrarTool:
    BUCKET_NAME = "muilyang12-nutrition-comparison"
    S3_DOMAIN = ""

    def __init__(self, app):
        self.app = app
        self.nutrition_facts_s3_url = None

        self.crawler_api = CrawlerApi()

        self.shift_pressed = False
        self.listener = keyboard.Listener(
            on_press=self.on_press, on_release=self.on_release
        )
        self.listener.start()

        self.s3_client = boto3.client("s3")

    def on_press(self, key):
        try:
            if key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
                self.shift_pressed = True

            # Ctrl + Shift + 1
            elif key.vk == 49 and self.shift_pressed:
                self.register_category()

            # Ctrl + Shift + 2
            elif key.vk == 50 and self.shift_pressed:
                self.register_product()

            # Ctrl + R
            elif key.char == "\x12" and self.shift_pressed:
                self.register_data()

        except AttributeError:
            pass

    def on_release(self, key):
        if key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
            self.shift_pressed = False

    def register_category(self):
        if self.app.current_category_id:
            return

        category_key, category_name = self.app.current_category
        res = self.crawler_api.register_food_category(category_key, category_name)
        self.app.current_category_id = res["id"]

        self.app.categories = self.app.crawler_api.get_food_categories()

    def register_product(self):
        print(self.app.current_category_id)

        focused_item = self.app.ui.tree.focus()
        values = self.app.ui.tree.item(focused_item, "values")

        brand_name = values[self.app.ui.column_index["brand_name"]]
        product_name = values[self.app.ui.column_index["product_name"]]
        coupang_url = values[self.app.ui.column_index["url"]]

        res = self.crawler_api.register_product(
            food_category=self.app.current_category_id,
            brand_name=brand_name,
            product_name=product_name,
            coupang_url=coupang_url,
        )
        self.app.target_product_id = res["id"]

    def register_data(self):
        values = self.app.selected_product_values
        row = [
            values[self.app.ui.column_index["category_key"]],
            values[self.app.ui.column_index["category_name"]],
            values[self.app.ui.column_index["brand_name"]],
            values[self.app.ui.column_index["product_name"]],
            values[self.app.ui.column_index["url"]],
        ]

        win32clipboard.OpenClipboard()
        try:
            clipboard_data = win32clipboard.GetClipboardData(win32clipboard.CF_TEXT)
        except TypeError:
            clipboard_data = win32clipboard.GetClipboardData(
                win32clipboard.CF_UNICODETEXT
            )
        except:
            print("There is an issue with the clipboard data format.")
        win32clipboard.CloseClipboard()

        clipboard_values = clipboard_data.split(",")

        # 값의 개수 확인
        if len(clipboard_values) != 15:
            print("There is an issue with the clipboard data format.")
        else:
            row.append(clipboard_values)

        with open("../result-data.csv", mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(row)

    def upload_nutrition_facts_image(self, screenshot):
        values = self.app.selected_product_values
        category_name = values[self.app.ui.column_index["category_name"]]
        product_name = values[self.app.ui.column_index["product_name"]]

        s3_key = get_path(category_name, product_name)

        with io.BytesIO() as output:
            screenshot.save(output, format="PNG")
            output.seek(0)

            self.s3_client.put_object(
                Bucket=self.BUCKET_NAME,
                Key=s3_key,
                Body=output,
                ContentType="image/png",
            )

            self.nutrition_facts_s3_url = (
                f"https://{self.BUCKET_NAME}.s3.amazonaws.com/{s3_key}"
            )
