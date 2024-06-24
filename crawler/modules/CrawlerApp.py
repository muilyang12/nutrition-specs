import tkinter as tk

from .CrawlerApi import CrawlerApi
from .CrawlerScreenshotTool import CrawlerScreenshotTool
from .CrawlerUI import CrawlerUI
from .CrawlerUIEvent import CrawlerUIEvent
from .CrawlerKeyEvent import CrawlerKeyEvent


class CrawlerApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Crawler")
        self.window.geometry("1000x600")

        self.crawler_api = CrawlerApi()

        self.screenshot_tool = CrawlerScreenshotTool(app=self)

        self.ui = CrawlerUI(self.window)
        self.ui_event = CrawlerUIEvent(app=self)

        self.key_event = CrawlerKeyEvent(app=self)

        self.selected_product_values = None

        self.categories = self.crawler_api.get_food_categories()
        self.current_category_id = None

    def start(self):
        self.window.mainloop()
