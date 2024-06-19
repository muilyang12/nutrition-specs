import tkinter as tk
import threading

from .. import (
    get_products,
    get_product_details,
    save_text_data,
    save_coupang_content_images,
    save_nutrition_facts,
)


def on_click_search(query_entry, key_entry, tree):
    thread = threading.Thread(
        target=on_click_search_core, args=(query_entry, key_entry, tree)
    )
    thread.start()


def on_click_search_core(query_entry, key_entry, tree):
    if len(query_entry.get()) == 0 or len(key_entry.get()) == 0:
        return

    for i in tree.get_children():
        tree.delete(i)

    products = get_products(search_tring=query_entry.get())

    for product in products:
        tree.insert(
            "",
            tk.END,
            values=(
                product["brand_name"],
                product["product_name"],
                product["url"],
            ),
        )

        product_name = product["product_name"]

        details = get_product_details(product=product)
        save_text_data(
            save_dir=f"./data/{product_name}/",
            file_name="details.json",
            data={"details": details},
            type="json",
        )
        save_coupang_content_images(save_dir=f"./data/{product_name}/", details=details)

        save_nutrition_facts(dir_path=f"./data/{product_name}/")

    query_entry.delete(0, tk.END)
    key_entry.delete(0, tk.END)
