import tkinter as tk
from pynput import keyboard
from PIL import ImageGrab

from .CrawlerDataRegistrar import CrawlerDataRegistrar


class CrawlerScreenshotTool:
    def __init__(self, app):
        self.app = app

        self.data_registrar = CrawlerDataRegistrar()
        self.result_screenshot = None

        with keyboard.GlobalHotKeys(
            {"<ctrl>+<shift>+s": self.start_screenshot_mode}
        ) as h:
            h.join()

    def start_screenshot_mode(self, event):
        overlay = tk.Toplevel(self.app.window)
        overlay.attributes("-fullscreen", True)
        overlay.attributes("-alpha", 0.3)
        overlay.attributes("-topmost", True)
        overlay.configure(bg="black")

        overlay.bind("<Button-1>", self.on_overlay_click)

    def on_overlay_click(self, event):
        DEVICE_PIXEL_RATIO = 1.65

        self.clicked_coordinates.append((event.x_root, event.y_root))

        if len(self.clicked_coordinates) == 2:
            event.widget.unbind("<Button-1>")
            event.widget.destroy()

            start, end = self.clicked_coordinates
            x_start = min(start[0], end[0]) * DEVICE_PIXEL_RATIO
            y_start = min(start[1], end[1]) * DEVICE_PIXEL_RATIO
            x_end = max(start[0], end[0]) * DEVICE_PIXEL_RATIO
            y_end = max(start[1], end[1]) * DEVICE_PIXEL_RATIO

            screenshot = ImageGrab.grab(bbox=(x_start, y_start, x_end, y_end))
            self.result_screenshot = screenshot

            self.result_screenshot.show()
            # self.register_data()

            self.clicked_coordinates = []

    def register_data(self):
        category_data = {}
        product_data = {}
        nutrition_data = {}

        self.data_registrar.register_food_category(data=category_data)
        self.data_registrar.register_product(data=product_data)
        self.data_registrar.register_nutrition(
            file_name="", screenshot=self.result_screenshot, data=nutrition_data
        )

        self.result_screenshot = None
        self.app.selected_product_values = None
