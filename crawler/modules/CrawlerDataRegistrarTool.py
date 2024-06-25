import io
import csv

import boto3
from pynput import keyboard
import win32clipboard

from .common import get_path


class CrawlerDataRegistrarTool:
    BUCKET_NAME = "muilyang12-nutrition-comparison"
    S3_DOMAIN = ""

    def __init__(self, app):
        self.app = app
        self.nutrition_facts_s3_url = None

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

            # Ctrl + Shift + 3
            elif key.vk == 51 and self.shift_pressed:
                self.register_nutrition()

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
        res = self.app.crawler_api.register_food_category(category_key, category_name)
        self.app.current_category_id = res["id"]

        self.app.categories = self.app.crawler_api.get_food_categories()

    def register_product(self):
        print(self.app.current_category_id)

        focused_item = self.app.ui.tree.focus()
        values = self.app.ui.tree.item(focused_item, "values")

        brand_name = values[self.app.ui.column_index["brand_name"]]
        product_name = values[self.app.ui.column_index["product_name"]]
        coupang_url = values[self.app.ui.column_index["url"]]

        res = self.app.crawler_api.register_product(
            food_category=self.app.current_category_id,
            brand_name=brand_name,
            product_name=product_name,
            coupang_url=coupang_url,
        )
        self.app.target_product_id = res["id"]

    def register_nutrition(self):
        win32clipboard.OpenClipboard()
        try:
            clipboard_data = win32clipboard.GetClipboardData(win32clipboard.CF_TEXT)
            clipboard_data = clipboard_data.decode("utf-8")
        except TypeError:
            clipboard_data = win32clipboard.GetClipboardData(
                win32clipboard.CF_UNICODETEXT
            )
        except:
            print("There is an issue with the clipboard data format.")
        win32clipboard.CloseClipboard()

        clipboard_values = clipboard_data.split(",")
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
        ) = clipboard_values

        res = self.app.crawler_api.register_nutrition(
            data={
                "product": self.app.target_product_id,
                "serving_size": serving_size if serving_size != "-" else None,
                "serving_unit": serving_unit if serving_unit != "-" else None,
                "calories": calories if calories != "-" else None,
                "total_carbohydrate": (
                    total_carbohydrate if total_carbohydrate != "-" else None
                ),
                "sugars": sugars if sugars != "-" else None,
                "sugar_alcohols": sugar_alcohols if sugar_alcohols != "-" else None,
                "dietary_fiber": dietary_fiber if dietary_fiber != "-" else None,
                "allulose": allulose if allulose != "-" else None,
                "total_fat": total_fat if total_fat != "-" else None,
                "saturated_fat": saturated_fat if saturated_fat != "-" else None,
                "trans_fat": trans_fat if trans_fat != "-" else None,
                "cholesterol": cholesterol if cholesterol != "-" else None,
                "protein": protein if protein != "-" else None,
                "sodium": sodium if sodium != "-" else None,
                "calcium": calcium if calcium != "-" else None,
            }
        )

    def upload_nutrition_facts_image(self, screenshot):
        focused_item = self.app.ui.tree.focus()
        values = self.app.ui.tree.item(focused_item, "values")

        category_name = values[self.app.ui.column_index["category_name"]]

        s3_key = get_path(category_name, f"{self.app.target_product_id}.png")

        with io.BytesIO() as output:
            screenshot.save(output, format="PNG")
            output.seek(0)

            self.s3_client.put_object(
                Bucket=self.BUCKET_NAME,
                Key=s3_key,
                Body=output,
                ContentType="image/png",
            )

            nutrition_facts_s3_url = (
                f"https://{self.BUCKET_NAME}.s3.amazonaws.com/{s3_key}"
            )

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
