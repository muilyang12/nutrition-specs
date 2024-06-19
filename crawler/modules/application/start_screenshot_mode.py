import tkinter as tk
from PIL import ImageGrab

from .close_window import close_window

clicks = []
DEVICE_PIXEL_RATIO = 1.5


def start_screenshot_mode(event):
    overlay = tk.Toplevel(event.widget)
    overlay.attributes("-fullscreen", True)
    overlay.attributes("-alpha", 0.3)  # Adjust the transparency level (0.0 to 1.0)
    overlay.attributes("-topmost", True)
    overlay.configure(bg="black")

    overlay.bind("<Button-1>", on_overlay_click)
    overlay.bind("<Control-q>", close_window)


def on_overlay_click(event):
    global clicks

    clicks.append((event.x_root, event.y_root))

    if len(clicks) == 2:
        event.widget.unbind("<Button-1>")
        event.widget.destroy()

        start, end = clicks
        x_start = min(start[0], end[0]) * DEVICE_PIXEL_RATIO
        y_start = min(start[1], end[1]) * DEVICE_PIXEL_RATIO
        x_end = max(start[0], end[0]) * DEVICE_PIXEL_RATIO
        y_end = max(start[1], end[1]) * DEVICE_PIXEL_RATIO

        screenshot = ImageGrab.grab(bbox=(x_start, y_start, x_end, y_end))
        screenshot.show()

        clicks = []
