import re
import os
import time
import uuid

from PIL import Image

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
        category_name = self.app.ui.category_entry.get().strip()

        s3_key = get_path(category_name, f"{uuid.uuid4()}.png")

        print(self.app.current_image, s3_key)
