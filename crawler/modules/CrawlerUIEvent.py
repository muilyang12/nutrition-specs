import tkinter as tk
from tkinter import messagebox
import threading
import webbrowser
import os
from PIL import Image

from .coupang_data import (
    get_products,
    get_product_details,
    save_coupang_content_images,
    save_nutrition_facts,
)
from .common import save_text_data


class CrawlerUIEvent:
    def __init__(self, window, ui):
        self.window = window
        self.ui = ui

        self.ui.query_button.config(command=self.on_click_search)
        self.ui.tree.bind("<Double-Button-1>", self.on_dbclick_treeview)

    def on_click_search(self):
        thread = threading.Thread(target=self.on_click_search_core)
        thread.start()

    def on_click_search_core(self):
        query = self.ui.query_entry.get()
        category_name = self.ui.name_entry.get()
        category_key = self.ui.key_entry.get()

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
                    "-",
                    product["url"],
                ),
            )

            product_name = product["product_name"]

            details = get_product_details(product=product)
            save_text_data(
                save_dir=f"./data/{category_name}/{product_name}/",
                file_name="details.json",
                data={"details": details},
                type="json",
            )
            save_coupang_content_images(
                save_dir=f"./data/{category_name}/{product_name}/", details=details
            )

            # save_nutrition_facts(dir_path=f"./data/{category_name}/{product_name}/")

        self.ui.query_entry.delete(0, tk.END)
        self.ui.name_entry.delete(0, tk.END)
        self.ui.key_entry.delete(0, tk.END)

    def on_dbclick_treeview(self, event):
        item = self.ui.tree.identify("item", event.x, event.y)

        column = self.ui.tree.identify_column(event.x)

        if not item or not column:
            return

        values = self.ui.tree.item(item, "values")

        if column == "#6":
            url = values[5]

            webbrowser.open(url)

        elif column == "#5":
            print(values)

            category_name = values[0]
            product_name = values[3]

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
