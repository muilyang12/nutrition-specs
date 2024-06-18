import tkinter as tk


def print_input(entry):
    print(entry.get())

    entry.delete(0, tk.END)


def open_ui():
    window = tk.Tk()
    window.title("Crawler")
    window.geometry("600x600")

    keyword_label = tk.Label(window, text="Keyword")
    keyword_label.grid(row=0, column=0, padx=10, pady=10)
    keyword_entry = tk.Entry(window)
    keyword_entry.grid(row=0, column=1, padx=10, pady=10)
    keyword_button = tk.Button(
        window, text="Search", command=lambda: print_input(keyword_entry)
    )
    keyword_button.grid(row=0, column=2, padx=10, pady=10)

    return window
