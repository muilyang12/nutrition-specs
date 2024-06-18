from .close_window import close_window
from .start_screenshot_mode import start_screenshot_mode


def bind_events(window):
    window.bind("<Control-q>", close_window)
    window.bind("<Control-s>", start_screenshot_mode)
