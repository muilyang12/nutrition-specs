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
        self.clicked_coordinates = []
        self.result_screenshot = None

        self.shift_pressed = False
        self.listener = keyboard.Listener(
            on_press=self.on_press, on_release=self.on_release
        )
        self.listener.start()

    def on_press(self, key):
        try:
            if key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
                self.shift_pressed = True
            # Ctrl + Z
            elif key.char == "\x1A" and self.shift_pressed:
                self.start_screenshot_mode()

        except AttributeError:
            pass

    def on_release(self, key):
        if key == keyboard.Key.shift_l or key == keyboard.Key.shift_r:
            self.shift_pressed = False

    def start_screenshot_mode(self):
        self.overlay = tk.Toplevel(self.app.window)
        self.overlay.attributes("-fullscreen", True)
        self.overlay.attributes("-alpha", 0.3)
        self.overlay.attributes("-topmost", True)
        self.overlay.configure(bg="black")

        self.overlay.bind("<Button-1>", self.on_overlay_click)

    def on_overlay_click(self, event):
        DEVICE_PIXEL_RATIO = 1.5

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
