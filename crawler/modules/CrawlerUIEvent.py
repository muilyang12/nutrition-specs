import threading
import webbrowser
import os
import time
import tkinter as tk
from tkinter import messagebox

from PIL import Image

from . import constants

from .coupang_data import (
    get_products,
    get_product_details,
    save_coupang_content_images,
    # save_nutrition_facts,
)
from .common import save_text_data, get_path


class CrawlerUIEvent:
    def __init__(self, app):
        self.app = app

        self.app.ui.search_button.config(command=self.on_click_search)
        self.app.ui.manual_collect_button.config(command=self.on_click_manual_collect)
        self.app.ui.semi_auto_collect_button.config(
            command=self.on_click_semi_auto_collect
        )
        self.app.ui.tree.bind("<Double-Button-1>", self.on_dbclick_treeview)

    def on_click_search(self):
        thread = threading.Thread(target=self.on_click_search_core)
        thread.start()

    def on_click_search_core(self):
        query = self.app.ui.query_entry.get().strip()
        category_name = self.app.ui.name_entry.get().strip()
        category_key = self.app.ui.key_entry.get().strip()

        self.app.current_category = (category_key, category_name)

        if len(query) == 0 or len(category_name) == 0 or len(category_key) == 0:
            return

        products = get_products(search_tring=query)

        for product in products:
            self.app.ui.tree.insert(
                "",
                tk.END,
                values=(
                    category_name,
                    category_key,
                    product["brand_name"],
                    product["product_name"],
                    "Manual Collect",
                    "-",
                    product["url"],
                ),
            )

            product_name = product["product_name"]

            details = get_product_details(product=product)
            save_text_data(
                save_dir=get_path("data", category_name, product_name),
                file_name="details.json",
                data={"details": details},
                type="json",
            )
            save_coupang_content_images(
                save_dir=get_path("data", category_name, product_name),
                details=details,
            )

        self.app.ui.query_entry.delete(0, tk.END)
        self.app.ui.name_entry.delete(0, tk.END)
        self.app.ui.key_entry.delete(0, tk.END)

    def on_click_manual_collect(self):
        children = self.app.ui.tree.get_children()

    def on_click_semi_auto_collect(self):
        children = self.app.ui.tree.get_children()

        for child in children:
            item = self.app.ui.tree.item(child)
            values = item["values"]
            category_name = values[self.app.ui.column_index["category_name"]]
            product_name = values[self.app.ui.column_index["product_name"]]

            # save_nutrition_facts(dir_path=get_path("data", category_name, product_name))

    def on_dbclick_treeview(self, event):
        item = self.app.ui.tree.identify("item", event.x, event.y)

        column = self.app.ui.tree.identify_column(event.x)

        if not item or not column:
            return

        values = self.app.ui.tree.item(item, "values")

        if column == f"#{self.app.ui.column_index['url'] + 1}":
            url = values[self.app.ui.column_index["url"]]

            webbrowser.open(url)

        elif column == f"#{self.app.ui.column_index['start_manual_collect'] + 1}":
            print("start_manual_collect", values)

            self.app.selected_product_values = values

            category_name = values[self.app.ui.column_index["category_name"]]
            product_name = values[self.app.ui.column_index["product_name"]]

            opened_image_count = 0
            for file_name in os.listdir(get_path("data", category_name, product_name)):
                if not file_name.split(".")[-1] in constants.IMAGE_EXTENSIONS:
                    continue

                image_path = get_path("data", category_name, product_name, file_name)
                img = Image.open(image_path)
                img.show()
                opened_image_count += 1

                time.sleep(0.3)

            if opened_image_count == 0:
                print("No image files found.")

        elif column == f"#{self.app.ui.column_index['nutrition_facts'] + 1}":
            print(values)

            category_name = values[self.app.ui.column_index["category_name"]]
            product_name = values[self.app.ui.column_index["product_name"]]

            nutrition_image_path = get_path(
                "data", category_name, product_name, "nutrition-facts-1.jpg"
            )

            if os.path.exists(nutrition_image_path):
                img = Image.open(nutrition_image_path)
                img.show()
            else:
                messagebox.showerror(
                    "Error",
                    f"nutrition-facts.jpg file for {product_name} does not exist.",
                )
