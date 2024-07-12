import tkinter as tk

from .DBHandlerUI import DBHandlerUI
from ..CrawlerScreenshotTool import CrawlerScreenshotTool


class DBHandlerApp:
    def __init__(self):
        self.current_image = None

        self.window = tk.Tk()
        self.window.title("DB Handler")
        self.window.geometry("1000x600")

        self.screenshot_tool = CrawlerScreenshotTool(app=self)

        self.ui = DBHandlerUI(app=self)

    def start(self):
        self.window.mainloop()
