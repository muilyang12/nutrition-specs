from modules import (
    get_products,
    save_product_details,
)

products = get_products(searchString="두유")

for product in products:
    save_product_details(product=product)
