from modules import (
    get_products,
    get_product_details,
    save_text_data,
)

products = get_products(searchString="두유")

for product in products:
    product_name = product["name"]

    details = get_product_details(product=product)
    save_text_data(
        save_dir=f"./data/{product_name}/",
        file_name="details.json",
        data={"details": details},
        type="json",
    )
