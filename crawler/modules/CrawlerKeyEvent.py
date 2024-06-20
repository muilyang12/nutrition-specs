import tkinter as tk
from PIL import ImageGrab


class CrawlerKeyEvent:
    def __init__(self, app):
        self.app = app

        self.app.window.bind("<Control-q>", self.close_window)
        self.app.window.bind("<Control-Return>", self.app.ui_event.on_click_search)

    def close_window(self, event):
        self.app.window.destroy()
