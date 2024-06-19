import tkinter as tk
from tkinter import ttk


class CrawlerUI:
    def __init__(self, window):
        self.window = window

        self.create_widgets()

    def create_widgets(self):
        self.query_label = tk.Label(self.window, text="Search Query")
        self.query_label.grid(row=0, column=0, padx=10, pady=10)
        self.query_entry = tk.Entry(self.window)
        self.query_entry.grid(row=0, column=1, padx=10, pady=10)

        self.name_label = tk.Label(self.window, text="Category Name")
        self.name_label.grid(row=1, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(self.window)
        self.name_entry.grid(row=1, column=1, padx=10, pady=10)

        self.key_label = tk.Label(self.window, text="Category Key")
        self.key_label.grid(row=2, column=0, padx=10, pady=10)
        self.key_entry = tk.Entry(self.window)
        self.key_entry.grid(row=2, column=1, padx=10, pady=10)

        self.search_button = tk.Button(self.window, text="Search")
        self.search_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        columns = (
            "category_name",
            "category_key",
            "brand_name",
            "product_name",
            "nutrition_facts",
            "url",
        )
        self.tree = ttk.Treeview(self.window, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col.replace("_", " ").title())
            self.tree.column(col, width=100, stretch=tk.YES)

        self.tree.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
