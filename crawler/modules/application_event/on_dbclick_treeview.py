import webbrowser
import os
from PIL import Image
from tkinter import messagebox

from ..image import compare_pillow_images


def on_dbclick_treeview(event, tree):
    item = tree.identify("item", event.x, event.y)
    column = tree.identify_column(event.x)

    if not item or not column:
        return

    values = tree.item(item, "values")

    if column == "#6":
        url = values[5]

        webbrowser.open(url)

    elif column == "#5":
        print(values)

        category_name = values[0]
        product_name = values[3]

        nutrition_image_path = (
            f"./data/{category_name}/{product_name}/nutrition-facts-1.jpg"
        )

        if os.path.exists(nutrition_image_path):
            img = Image.open(nutrition_image_path)
            img.show()
        else:
            messagebox.showerror(
                "Error", f"nutrition-facts.jpg file for {product_name} does not exist."
            )
