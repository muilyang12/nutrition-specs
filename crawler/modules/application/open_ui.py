import tkinter as tk
from tkinter import ttk

from ..get_products import get_products


def on_click_search(query_entry, key_entry, tree):
    if len(query_entry.get()) == 0 or len(key_entry.get()) == 0:
        return

    products = get_products(search_tring="두유")
    print(products)

    print(query_entry.get())
    print(key_entry.get())

    for i in tree.get_children():
        tree.delete(i)

    for product in products:
        tree.insert(
            "",
            tk.END,
            values=(
                product["name"],
                product["url"],
            ),
        )

    query_entry.delete(0, tk.END)
    key_entry.delete(0, tk.END)


def open_ui():
    window = tk.Tk()
    window.title("Crawler")
    window.geometry("1000x600")

    query_label = tk.Label(window, text="Search Query")
    query_label.grid(row=0, column=0, padx=10, pady=10)
    query_entry = tk.Entry(window)
    query_entry.grid(row=0, column=1, padx=10, pady=10)

    key_label = tk.Label(window, text="Category Key")
    key_label.grid(row=1, column=0, padx=10, pady=10)
    key_entry = tk.Entry(window)
    key_entry.grid(row=1, column=1, padx=10, pady=10)

    query_button = tk.Button(
        window,
        text="Search",
        command=lambda: on_click_search(query_entry, key_entry, tree),
    )
    query_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    columns = ("name", "url")
    tree = ttk.Treeview(window, columns=columns, show="headings")
    tree.heading("name", text="Name")
    tree.heading("url", text="URL")

    tree.column("name", stretch=tk.YES)
    tree.column("url", stretch=tk.YES)

    tree.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    return window
