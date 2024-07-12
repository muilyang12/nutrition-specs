import tkinter as tk
from tkinter import ttk

from .DBHandle import DBHandle


class DBHandlerUI:
    def __init__(self, app):
        self.app = app

        self.dbHandle = DBHandle("../be/db.sqlite3")
        self.dbHandle.connect()

        self.inputs = []

        self.create_widgets()
        self.load_values()

    def create_widgets(self):
        columns = self.dbHandle.get_column_names("food_product")

        self.columns = tuple(columns)
        self.column_index = {col: idx for idx, col in enumerate(self.columns)}
        self.tree = ttk.Treeview(self.app.window, columns=self.columns, show="headings")

        for col in self.columns:
            self.tree.heading(col, text=col.replace("_", " ").title())

            if col == "product_name":
                self.tree.column(col, width=200, stretch=tk.YES)
            else:
                self.tree.column(col, width=100, stretch=tk.YES)

        self.tree.grid(row=0, column=0, columnspan=7, padx=10, pady=10, sticky="nsew")

        self.category_label = tk.Label(self.app.window, text="Category Name")
        self.category_label.grid(row=1, column=0, padx=10, pady=10)
        self.category_entry = tk.Entry(self.app.window)
        self.category_entry.grid(row=1, column=1, padx=10, pady=10)

        self.add_ingredients_button = tk.Button(
            self.app.window, text="Start getting ingredients"
        )
        self.add_ingredients_button.grid(row=1, column=2, padx=10, pady=10)

        self.upload_ingredients_button = tk.Button(
            self.app.window, text="Upload ingredients"
        )
        self.upload_ingredients_button.grid(row=1, column=3, padx=10, pady=10)

    def load_values(self):
        table_data = self.dbHandle.get_table_data("food_product")

        for data in table_data:
            self.tree.insert(
                "",
                tk.END,
                values=data,
            )
