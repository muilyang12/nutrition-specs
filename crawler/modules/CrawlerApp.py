import tkinter as tk

from .CrawlerApi import CrawlerApi
from .CrawlerScreenshotTool import CrawlerScreenshotTool
from .CrawlerUI import CrawlerUI
from .CrawlerUIEvent import CrawlerUIEvent
from .CrawlerKeyEvent import CrawlerKeyEvent


class CrawlerApp:
    def __init__(self):
        self.category_mapper = {}

        self.window = tk.Tk()
        self.window.title("Crawler")
        self.window.geometry("1000x600")

        self.crawler_api = CrawlerApi()

        self.screenshot_tool = CrawlerScreenshotTool(app=self)

        self.ui = CrawlerUI(app=self)
        self.ui_event = CrawlerUIEvent(app=self)

        self.key_event = CrawlerKeyEvent(app=self)

        self.selected_product_values = None

        self.categories = self.crawler_api.get_food_categories()
        self.brands = None
        self.current_category = None
        self.current_category_id = None
        self.target_product_id = None
        self.target_nutrition_s3 = None

    def start(self):
        self.window.mainloop()
