import tkinter as tk
from tkinter import ttk


class CrawlerUI:
    def __init__(self, window):
        self.window = window

        self.create_widgets()

    def create_widgets(self):
        self.name_label = tk.Label(self.window, text="Category Name")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(self.window)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.key_label = tk.Label(self.window, text="Category Key")
        self.key_label.grid(row=0, column=2, padx=10, pady=10)
        self.key_entry = tk.Entry(self.window)
        self.key_entry.grid(row=0, column=3, padx=10, pady=10)

        self.category_button = tk.Button(self.window, text="Add Category")
        self.category_button.grid(row=0, column=4, padx=10, pady=10)

        self.category_listbox = tk.Listbox(self.window, selectmode=tk.MULTIPLE)
        self.category_listbox.grid(row=0, column=5, padx=1, pady=10)

        # =========================

        self.brand_name_label = tk.Label(self.window, text="Brand Name")
        self.brand_name_label.grid(row=1, column=0, padx=10, pady=10)
        self.brand_name_entry = tk.Entry(self.window)
        self.brand_name_entry.grid(row=1, column=1, padx=10, pady=10)

        self.brand_button = tk.Button(self.window, text="Add Brand")
        self.brand_button.grid(row=1, column=4, padx=10, pady=10)

        self.brand_combobox = ttk.Combobox(self.window, values=["QQQQQ", "WWWWW"])
        self.brand_combobox.grid(row=1, column=5, columnspan=2, padx=10, pady=10)

        # =========================

        self.query_label = tk.Label(self.window, text="Search Query")
        self.query_label.grid(row=2, column=0, padx=10, pady=10)
        self.query_entry = tk.Entry(self.window)
        self.query_entry.grid(row=2, column=1, padx=10, pady=10)

        self.search_button = tk.Button(self.window, text="Search")
        self.search_button.grid(row=2, column=4, columnspan=2, padx=10, pady=10)

        # =========================

        self.manual_collect_button = tk.Button(self.window, text="Manual Collecting")
        self.manual_collect_button.grid(row=3, column=0, padx=10, pady=10)

        self.semi_auto_collect_button = tk.Button(
            self.window, text="Semi-Auto Collecting"
        )
        self.semi_auto_collect_button.grid(row=3, column=1, padx=10, pady=10)

        # =========================

        self.columns = (
            "category_name",
            "category_key",
            "brand_name",
            "product_name",
            "start_manual_collect",
            "nutrition_facts",
            "url",
        )
        self.column_index = {col: idx for idx, col in enumerate(self.columns)}
        self.tree = ttk.Treeview(self.window, columns=self.columns, show="headings")

        for col in self.columns:
            self.tree.heading(col, text=col.replace("_", " ").title())

            if col == "product_name":
                self.tree.column(col, width=200, stretch=tk.YES)
            else:
                self.tree.column(col, width=100, stretch=tk.YES)

        self.tree.grid(row=4, column=0, columnspan=7, padx=10, pady=10, sticky="nsew")
