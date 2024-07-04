import tkinter as tk

from .CrawlerApi import CrawlerApi
from .CrawlerScreenshotTool import CrawlerScreenshotTool
from .CrawlerUI import CrawlerUI
from .CrawlerUIEvent import CrawlerUIEvent
from .CrawlerKeyEvent import CrawlerKeyEvent


class CrawlerApp:
    def __init__(self):
        self.categories_mapper = {}
        self.brands_mapper = {}
        self.current_image = None

        self.window = tk.Tk()
        self.window.title("Crawler")
        self.window.geometry("1000x600")

        self.crawler_api = CrawlerApi()

        self.screenshot_tool = CrawlerScreenshotTool(app=self)

        self.ui = CrawlerUI(app=self)
        self.ui_event = CrawlerUIEvent(app=self)

        self.key_event = CrawlerKeyEvent(app=self)

    def start(self):
        self.window.mainloop()
