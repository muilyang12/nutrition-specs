import tkinter as tk

from .CrawlerScreenshotTool import CrawlerScreenshotTool
from .CrawlerUI import CrawlerUI
from .CrawlerUIEvent import CrawlerUIEvent
from .CrawlerKeyEvent import CrawlerKeyEvent


class CrawlerApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Crawler")
        self.window.geometry("1000x600")

        self.screenshot_tool = CrawlerScreenshotTool(self.window)

        self.ui = CrawlerUI(self.window)
        self.ui_event = CrawlerUIEvent(self.window, self.ui)
        self.key_Event = CrawlerKeyEvent(self.window)

    def start(self):
        self.window.mainloop()
