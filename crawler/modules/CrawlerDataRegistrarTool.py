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

        self.current_brand_id = None

    def on_press(self, key):
        try:
            if key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
                self.shift_pressed = True

            # Ctrl + Shift + 4
            elif key.vk == 52 and self.shift_pressed:
                self.register_nutrition()

            # Ctrl + Shift + R
            elif key.char == "\x12" and self.shift_pressed:
                self.register_data()

        except AttributeError:
            pass

    def on_release(self, key):
        if key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
            self.shift_pressed = False

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

        res = self.app.crawler_api.register_nutrition(
            product_id=self.app.target_product_id,
            data=clipboard_data,
            s3_url=self.app.target_nutrition_s3,
        )

    def upload_nutrition_facts_image(self, screenshot):
        focused_item = self.app.ui.tree.focus()
        values = self.app.ui.tree.item(focused_item, "values")

        product_id = values[self.app.ui.column_index["product_id"]]

        selected_indices = self.app.ui.category_listbox.curselection()
        selected_categories = [
            self.app.ui.category_listbox.get(i) for i in selected_indices
        ]

        category_name = selected_categories[0]

        s3_key = get_path(category_name, f"{product_id}.png")

        with io.BytesIO() as output:
            screenshot.save(output, format="PNG")
            output.seek(0)

            self.s3_client.put_object(
                Bucket=self.BUCKET_NAME,
                Key=s3_key,
                Body=output,
                ContentType="image/png",
            )

            self.app.target_nutrition_s3 = (
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
            clipboard_data = clipboard_data.decode("utf-8")
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
