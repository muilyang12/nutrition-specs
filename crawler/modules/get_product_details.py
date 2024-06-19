from .coupang_api import coupang_get_with_headers


def get_product_details(product):
    productId, itemId, vendorItemId = (
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

    else:
        print("details 속성이 응답에 없습니다.")

        details = ""

    return details
