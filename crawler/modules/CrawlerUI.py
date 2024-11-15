import tkinter as tk
from tkinter import ttk


class CrawlerUI:
    def __init__(self, app):
        self.app = app

        self.create_widgets()
        self.initialize_category_options()

    def create_widgets(self):
        self.name_label = tk.Label(self.app.window, text="Category Name")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(self.app.window)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.key_label = tk.Label(self.app.window, text="Category Key")
        self.key_label.grid(row=0, column=2, padx=10, pady=10)
        self.key_entry = tk.Entry(self.app.window)
        self.key_entry.grid(row=0, column=3, padx=10, pady=10)

        self.category_button = tk.Button(self.app.window, text="Add Category")
        self.category_button.grid(row=0, column=4, padx=10, pady=10)

        self.category_listbox = tk.Listbox(self.app.window, selectmode=tk.MULTIPLE)
        self.category_listbox.grid(row=0, column=5, padx=1, pady=10)

        # =========================

        self.brand_name_label = tk.Label(self.app.window, text="Brand Name")
        self.brand_name_label.grid(row=1, column=0, padx=10, pady=10)
        self.brand_name_entry = tk.Entry(self.app.window)
        self.brand_name_entry.grid(row=1, column=1, padx=10, pady=10)

        self.brand_add_button = tk.Button(self.app.window, text="Add Brand")
        self.brand_add_button.grid(row=1, column=3, padx=10, pady=10)

        self.brand_get_button = tk.Button(self.app.window, text="Get Brands")
        self.brand_get_button.grid(row=1, column=4, padx=10, pady=10)

        self.brand_combobox = ttk.Combobox(self.app.window, values=["QQQQQ", "WWWWW"])
        self.brand_combobox.grid(row=1, column=5, columnspan=2, padx=10, pady=10)

        # =========================

        self.query_label = tk.Label(self.app.window, text="Search Query")
        self.query_label.grid(row=2, column=0, padx=10, pady=10)
        self.query_entry = tk.Entry(self.app.window)
        self.query_entry.grid(row=2, column=1, padx=10, pady=10)

        self.search_button = tk.Button(self.app.window, text="Search")
        self.search_button.grid(row=2, column=2, columnspan=2, padx=10, pady=10)

        # =========================

        self.add_product_button = tk.Button(self.app.window, text="Add Product")
        self.add_product_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.add_nutri_button = tk.Button(self.app.window, text="Add Nutrition")
        self.add_nutri_button.grid(row=3, column=2, columnspan=2, padx=10, pady=10)

        # =========================

        # self.manual_collect_button = tk.Button(
        #     self.app.window, text="Manual Collecting"
        # )
        # self.manual_collect_button.grid(row=3, column=0, padx=10, pady=10)

        # self.semi_auto_collect_button = tk.Button(
        #     self.app.window, text="Semi-Auto Collecting"
        # )
        # self.semi_auto_collect_button.grid(row=3, column=1, padx=10, pady=10)

        # =========================

        self.columns = (
            "product_id",
            "brand_name",
            "product_name",
            "start_manual_collect",
            "nutrition_facts",
            "url",
        )
        self.column_index = {col: idx for idx, col in enumerate(self.columns)}
        self.tree = ttk.Treeview(self.app.window, columns=self.columns, show="headings")

        for col in self.columns:
            self.tree.heading(col, text=col.replace("_", " ").title())

            if col == "product_name":
                self.tree.column(col, width=200, stretch=tk.YES)
            else:
                self.tree.column(col, width=100, stretch=tk.YES)

        self.tree.grid(row=4, column=0, columnspan=7, padx=10, pady=10, sticky="nsew")

    def initialize_category_options(self):
        categories_res = self.app.crawler_api.get_food_categories()

        for category_res in categories_res:
            category_name = category_res["category_name"]
            category_key = category_res["category_key"]
            category_id = category_res["id"]

            self.app.categories_mapper[category_name] = (
                category_id,
                category_name,
                category_key,
            )

            self.category_listbox.insert(tk.END, category_name)

    def refresh_category_options(self):
        self.app.categories_mapper = {}
        self.category_listbox.delete(0, tk.END)

        self.initialize_category_options()

    def refresh_brand_options(self):
        self.app.brands_mapper = {}

        selected_indices = self.app.ui.category_listbox.curselection()
        selected_categories = [
            self.app.ui.category_listbox.get(i) for i in selected_indices
        ]

        if len(selected_categories) != 1:
            print("Please select only one category.")

            return

        category_name = selected_categories[0]
        category_id = self.app.categories_mapper[category_name][0]
        brand_res = self.app.crawler_api.get_brands(category_id)

        brands = []
        for brand in brand_res:
            brand_name = brand["name"]
            brand_id = brand["id"]

            brands.append(brand_name)
            self.app.brands_mapper[brand_name] = (
                brand_name,
                brand_id,
            )

        self.brand_combobox["value"] = brands
