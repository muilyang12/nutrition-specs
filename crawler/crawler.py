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
