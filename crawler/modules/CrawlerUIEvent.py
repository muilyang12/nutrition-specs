import threading
import webbrowser
import os
import tkinter as tk
from tkinter import messagebox

from PIL import Image

from . import constants

from .coupang_data import (
    get_products,
    get_product_details,
    save_coupang_content_images,
    save_nutrition_facts,
)
from .common import save_text_data, replace_invalid_chars_for_directory


class CrawlerUIEvent:
    def __init__(self, window, ui):
        self.window = window
        self.ui = ui

        self.ui.search_button.config(command=self.on_click_search)
        self.ui.manual_collect_button.config(command=self.on_click_manual_collect)
        self.ui.semi_auto_collect_button.config(command=self.on_click_semi_auto_collect)
        self.ui.tree.bind("<Double-Button-1>", self.on_dbclick_treeview)

    def on_click_search(self):
        thread = threading.Thread(target=self.on_click_search_core)
        thread.start()

    def on_click_search_core(self):
        query = self.ui.query_entry.get().strip()
        category_name = self.ui.name_entry.get().strip()
        category_key = self.ui.key_entry.get().strip()

        if len(query) == 0 or len(category_name) == 0 or len(category_key) == 0:
            return

        products = get_products(search_tring=query)

        for product in products:
            self.ui.tree.insert(
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
                save_dir=f"./data/{category_name}/{replace_invalid_chars_for_directory(product_name)}/",
                file_name="details.json",
                data={"details": details},
                type="json",
            )
            save_coupang_content_images(
                save_dir=f"./data/{category_name}/{replace_invalid_chars_for_directory(product_name)}/",
                details=details,
            )

        self.ui.query_entry.delete(0, tk.END)
        self.ui.name_entry.delete(0, tk.END)
        self.ui.key_entry.delete(0, tk.END)

    def on_click_manual_collect(self):
        children = self.ui.tree.get_children()

    def on_click_semi_auto_collect(self):
        children = self.ui.tree.get_children()

        for child in children:
            item = self.ui.tree.item(child)
            values = item["values"]
            category_name = values[self.ui.column_index["category_name"]]
            product_name = values[self.ui.column_index["product_name"]]

            save_nutrition_facts(
                dir_path=f"./data/{category_name}/{replace_invalid_chars_for_directory(product_name)}/"
            )

    def on_dbclick_treeview(self, event):
        item = self.ui.tree.identify("item", event.x, event.y)

        column = self.ui.tree.identify_column(event.x)

        if not item or not column:
            return

        values = self.ui.tree.item(item, "values")

        if column == f"#{self.ui.column_index['url'] + 1}":
            url = values[5]

            webbrowser.open(url)

        elif column == f"#{self.ui.column_index['start_manual_collect'] + 1}":
            print("start_manual_collect", values)

            category_name = values[self.ui.column_index["category_name"]]
            product_name = values[self.ui.column_index["product_name"]]

            for file_name in os.listdir(f"./data/{category_name}/{product_name}/"):
                if not file_name.split(".")[-1] in constants.IMAGE_EXTENSIONS:
                    continue

                image_path = f"./data/{category_name}/{product_name}/{file_name}"
                img = Image.open(image_path)
                img.show()

        elif column == f"#{self.ui.column_index['nutrition_facts'] + 1}":
            print(values)

            category_name = values[self.ui.column_index["category_name"]]
            product_name = values[self.ui.column_index["product_name"]]

            nutrition_image_path = (
                f"./data/{category_name}/{product_name}/nutrition-facts-1.jpg"
            )

            if os.path.exists(nutrition_image_path):
                img = Image.open(nutrition_image_path)
                img.show()
            else:
                messagebox.showerror(
                    "Error",
                    f"nutrition-facts.jpg file for {product_name} does not exist.",
                )
