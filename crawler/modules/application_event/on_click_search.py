import tkinter as tk

from ..get_products import get_products


def on_click_search(query_entry, key_entry, tree):
    if len(query_entry.get()) == 0 or len(key_entry.get()) == 0:
        return

    products = get_products(search_tring=query_entry.get())

    for i in tree.get_children():
        tree.delete(i)

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

    query_entry.delete(0, tk.END)
    key_entry.delete(0, tk.END)
