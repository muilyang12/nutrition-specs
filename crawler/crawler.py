from modules import (
    application,
    # get_product_details,
    # save_text_data,
    # save_coupang_content_images,
    # save_nutrition_facts,
)

window = application.open_ui()

application.bind_events(window)

window.mainloop()

# for product in products:
#     product_name = product["name"]

#     details = get_product_details(product=product)
#     save_text_data(
#         save_dir=f"./data/{product_name}/",
#         file_name="details.json",
#         data={"details": details},
#         type="json",
#     )
#     save_coupang_content_images(save_dir=f"./data/{product_name}/", details=details)

#     save_nutrition_facts(dir_path=f"./data/{product_name}/")


# from PIL import ImageGrab


# def show_input():
#     entered_text = entry.get()
#     print(entered_text)
#     entry.delete(0, "end")


# def screenshot_mode(event):
#     window.iconify()  # Minimize window
#     x0, y0, x1, y1 = 100, 100, 500, 500
#     screenshot = ImageGrab.grab(bbox=(x0, y0, x1, y1))


# def close_window(event):
#     window.destroy()


# window.bind("<Control-q>", close_window)
# window.bind("<Control-s>", screenshot_mode)
