import re
import os
import time
import uuid
import json
from tkinter import messagebox

from PIL import Image
import win32clipboard

from ..coupang_data import get_product_details, save_coupang_content_images
from ..common import get_path
from .. import constants


class DBHandlerUIEvent:
    def __init__(self, app):
        self.app = app

        self.app.ui.add_ingredients_button.config(command=self.on_click_add_ingredients)
        self.app.ui.upload_ingredients_button.config(
            command=self.on_click_upload_ingredients
        )
        self.app.ui.upload_ingredient_info_button.config(
            command=self.on_click_upload_ingredient_info
        )

        self.initialize_ingreddients()

    def on_click_add_ingredients(self):
        focused_item = self.app.ui.tree.focus()
        values = self.app.ui.tree.item(focused_item, "values")

        product_name = values[1]
        url = values[2]

        product_id, item_id, vendor_item_id = self.get_product_info_from_url(url)

        details = get_product_details(product_id, item_id, vendor_item_id)
        save_coupang_content_images(
            save_dir=get_path("data", "---Retry", product_name),
            details=details,
        )

        opened_image_count = 0
        for file_name in os.listdir(get_path("data", "---Retry", product_name)):
            if not file_name.split(".")[-1] in constants.IMAGE_EXTENSIONS:
                continue

            image_path = get_path("data", "---Retry", product_name, file_name)
            img = Image.open(image_path)
            img.show()
            opened_image_count += 1

            time.sleep(0.5)

        if opened_image_count == 0:
            print("No image files found.")

    def get_product_info_from_url(self, url):
        pattern = re.compile(r"products/(\d+)\?itemId=(\d+)&vendorItemId=(\d+)")
        match = pattern.search(url)

        product_id = match.group(1)
        item_id = match.group(2)
        vendor_item_id = match.group(3)

        return [product_id, item_id, vendor_item_id]

    def on_click_upload_ingredients(self):
        focused_item = self.app.ui.tree.focus()
        values = self.app.ui.tree.item(focused_item, "values")

        product_id = values[0]

        category_name = self.app.ui.category_entry.get().strip()

        win32clipboard.OpenClipboard()
        try:
            clipboard_data = win32clipboard.GetClipboardData(win32clipboard.CF_TEXT)
            clipboard_data = clipboard_data.decode("euc-kr")
        except TypeError:
            clipboard_data = win32clipboard.GetClipboardData(
                win32clipboard.CF_UNICODETEXT
            )
        except:
            print("There is an issue with the clipboard data format.")
        win32clipboard.CloseClipboard()

        ingredient_categories = json.loads(clipboard_data)

        not_added_ingredients = []

        for values in ingredient_categories.values():
            for i in range(len(values)):
                if not values[i] in self.app.ingredients:
                    not_added_ingredients.append(values[i])

                    continue

                values[i] = self.app.ingredients[values[i]]

        messagebox.showinfo("Info", f"Not added ingredients: {not_added_ingredients}")
        print(f"Not added ingredients: {not_added_ingredients}")

        s3_key = get_path(category_name, f"{uuid.uuid4()}.png")

        self.app.api.register_product_ingredient(
            product_id=product_id,
            ingredients=[],
            ingredient_categories=ingredient_categories,
            s3_key=s3_key,
        )

        self.app.api.upload_image_to_s3(
            s3_key=s3_key, screenshot=self.app.current_image
        )

    def on_click_upload_ingredient_info(self):
        name = self.app.ui.ingredient_name_entry.get().strip()
        description = self.app.ui.ingredient_descriptioon_entry.get().strip()

        self.app.api.register_ingredient(name, description)

    def initialize_ingreddients(self):
        ingredients = self.app.api.get_ingredients()

        for data in ingredients:
            id = data["id"]
            name = data["name"]

            self.app.ingredients[name] = id
