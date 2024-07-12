import tkinter as tk
from tkinter import ttk


class DBHandlerUI:
    def __init__(self, app):
        self.app = app

        self.create_widgets()

    def create_widgets(self):
        self.name_label = tk.Label(self.app.window, text="Category Name")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(self.app.window)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)
