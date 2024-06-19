import tkinter as tk
import threading

from .. import (
    get_products,
    get_product_details,
    save_text_data,
    save_coupang_content_images,
    save_nutrition_facts,
)


def on_click_search(query_entry, name_entry, key_entry, tree):
    thread = threading.Thread(
        target=on_click_search_core, args=(query_entry, name_entry, key_entry, tree)
    )
    thread.start()


def on_click_search_core(query_entry, name_entry, key_entry, tree):
    query = query_entry.get()
    category_name = name_entry.get()
    category_key = key_entry.get()

    if len(query) == 0 or len(category_name) == 0 or len(category_key) == 0:
        return

    for i in tree.get_children():
        tree.delete(i)

    products = get_products(search_tring=query)

    for product in products:
        tree.insert(
            "",
            tk.END,
            values=(
                category_name,
                category_key,
                product["brand_name"],
                product["product_name"],
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

        save_nutrition_facts(dir_path=f"./data/{category_name}/{product_name}/")

    query_entry.delete(0, tk.END)
    key_entry.delete(0, tk.END)
