import tkinter as tk
from tkinter import ttk

from ..application_event import on_click_search, on_dbclick_treeview


def open_ui():
    window = tk.Tk()
    window.title("Crawler")
    window.geometry("1000x600")

    query_label = tk.Label(window, text="Search Query")
    query_label.grid(row=0, column=0, padx=10, pady=10)
    query_entry = tk.Entry(window)
    query_entry.grid(row=0, column=1, padx=10, pady=10)

    name_label = tk.Label(window, text="Category Name")
    name_label.grid(row=1, column=0, padx=10, pady=10)
    name_entry = tk.Entry(window)
    name_entry.grid(row=1, column=1, padx=10, pady=10)

    key_label = tk.Label(window, text="Category Key")
    key_label.grid(row=2, column=0, padx=10, pady=10)
    key_entry = tk.Entry(window)
    key_entry.grid(row=2, column=1, padx=10, pady=10)

    query_button = tk.Button(
        window,
        text="Search",
        command=lambda: on_click_search(query_entry, name_entry, key_entry, tree),
    )
    query_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    columns = (
        "category_name",
        "category_key",
        "brand_name",
        "product_name",
        "nutrition_facts",
        "url",
    )
    tree = ttk.Treeview(window, columns=columns, show="headings")

    tree.heading("category_name", text="Category Name")
    tree.heading("category_key", text="Category Key")
    tree.heading("brand_name", text="Brand Name")
    tree.heading("product_name", text="Product Name")
    tree.heading("nutrition_facts", text="Nutrition Facts")
    tree.heading("url", text="URL")

    tree.column("category_name", width=100, stretch=tk.YES)
    tree.column("category_key", width=100, stretch=tk.YES)
    tree.column("brand_name", width=100, stretch=tk.YES)
    tree.column("product_name", width=200, stretch=tk.YES)
    tree.column("nutrition_facts", width=100, stretch=tk.YES)
    tree.column("url", width=100, stretch=tk.YES)

    tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    tree.bind("<Double-Button-1>", lambda event: on_dbclick_treeview(event, tree))

    return window
