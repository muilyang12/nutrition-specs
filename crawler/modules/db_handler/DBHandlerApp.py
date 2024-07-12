import tkinter as tk

from .DBHandlerUI import DBHandlerUI


class DBHandlerApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("DB Handler")
        self.window.geometry("1000x600")

        self.ui = DBHandlerUI(app=self)

    def start(self):
        self.window.mainloop()
