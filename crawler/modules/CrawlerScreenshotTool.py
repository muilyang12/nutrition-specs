import tkinter as tk
from io import BytesIO

from pynput import keyboard
from PIL import ImageGrab
import win32clipboard

from .CrawlerDataRegistrarTool import CrawlerDataRegistrarTool


class CrawlerScreenshotTool:
    def __init__(self, app):
        self.app = app

        self.data_registrar = CrawlerDataRegistrarTool(app=self.app)
        self.result_screenshot = None

        with keyboard.GlobalHotKeys(
            {
                "<ctrl>+<shift>+s": self.start_screenshot_mode,
            }
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

        if len(self.clicked_coordinates) < 2:
            return

        event.widget.unbind("<Button-1>")
        event.widget.destroy()

        start, end = self.clicked_coordinates
        x_start = min(start[0], end[0]) * DEVICE_PIXEL_RATIO
        y_start = min(start[1], end[1]) * DEVICE_PIXEL_RATIO
        x_end = max(start[0], end[0]) * DEVICE_PIXEL_RATIO
        y_end = max(start[1], end[1]) * DEVICE_PIXEL_RATIO

        screenshot = ImageGrab.grab(bbox=(x_start, y_start, x_end, y_end))

        self.copy_to_clipboard(screenshot)
        screenshot.show()
        # self.data_registrar.register_data()

        self.clicked_coordinates = []

    def copy_to_clipboard(self, screenshot):
        output = BytesIO()
        screenshot.save(output, "BMP")
        data = output.getvalue()[14:]  # BMP 파일 헤더 부분 제거
        output.close()

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()
