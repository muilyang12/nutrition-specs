import io
import csv

import boto3
from pynput import keyboard
import win32clipboard


class CrawlerDataRegistrarTool:
    S3_DOMAIN = ""

    def __init__(self, app):
        self.app = app

        self.shift_pressed = False
        self.listener = keyboard.Listener(
            on_press=self.on_press, on_release=self.on_release
        )
        self.listener.start()

    def on_press(self, key):
        try:
            if key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
                self.shift_pressed = True
            # Ctrl + R
            elif key.char == "\x12" and self.shift_pressed:
                self.register_data()

        except AttributeError:
            pass

    def on_release(self, key):
        if key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
            self.shift_pressed = False

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
