import os
import json

from .coupang_get_with_headers import coupang_get_with_headers


def save_product_details(product):

    name, productId, itemId, vendorItemId = (
        product["name"],
        product["productId"],
        product["itemId"],
        product["vendorItemId"],
    )

    response = coupang_get_with_headers(
        f"https://www.coupang.com/vp/products/{productId}/items/{itemId}/vendoritems/{vendorItemId}"
    )
    data = response.json()

    if "details" in data:
        details = data["details"]

        save_dir = os.path.join(".", "data")
        product_name_dir = os.path.join(save_dir, name)
        os.makedirs(product_name_dir, exist_ok=True)

        file_path = os.path.join(product_name_dir, "details.json")
        with open(file_path, "w", encoding="utf-8") as file:
            details_dict = {"details": details}
            json.dump(details_dict, file, ensure_ascii=False, indent=4)

    else:
        print("details 속성이 응답에 없습니다.")
