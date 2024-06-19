import tkinter as tk
from PIL import ImageGrab


class CrawlerKeyEvent:
    def __init__(self, window):
        self.window = window
        self.clicked_coordinates = []

        self.window.bind("<Control-q>", self.close_window)
        self.window.bind("<Control-s>", self.start_screenshot_mode)

    def close_window(self, event):
        self.window.destroy()

    def start_screenshot_mode(self, event):
        overlay = tk.Toplevel(self.window)
        overlay.attributes("-fullscreen", True)
        overlay.attributes("-alpha", 0.3)  # Adjust the transparency level (0.0 to 1.0)
        overlay.attributes("-topmost", True)
        overlay.configure(bg="black")

        overlay.bind("<Button-1>", self.on_overlay_click)
        overlay.bind("<Control-q>", self.close_window)

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
            screenshot.show()

            self.clicked_coordinates = []
