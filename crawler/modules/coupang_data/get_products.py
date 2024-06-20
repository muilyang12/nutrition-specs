import re

from bs4 import BeautifulSoup

from ..coupang_api import coupang_get_with_headers, constants


def get_products(search_tring: str):
    product_data = []

    response = coupang_get_with_headers(
        f"https://www.coupang.com/np/search?q={search_tring}"
    )

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        products = soup.select(".search-product")

        for product in products:
            a_tag = product.select_one("a")
            name_tag = product.select_one("div.name")
            rating_tag = product.select_one("em.rating")
            rating_count_tag = product.select_one("span.rating-total-count")

            url = None
            productId = None
            itemId = None
            vendorItemId = None

            if a_tag:
                href = a_tag.get("href")
                url = (constants.COUPANG_DOMAIN + href) if href else None

                pattern = re.compile(r"products/(\d+)\?itemId=(\d+)&vendorItemId=(\d+)")
                match = pattern.search(url)
                if match:
                    productId = match.group(1)
                    itemId = match.group(2)
                    vendorItemId = match.group(3)

            if name_tag:
                name_tag_value = name_tag.text.strip().replace(",", "")
                splited_space = name_tag_value.split(" ")
                splited_space.pop()

                brand_name = splited_space.pop(0).strip("[]")
                product_name = " ".join(splited_space)

            product_data.append(
                {
                    "url": url,
                    "brand_name": brand_name,
                    "product_name": product_name,
                    "rating": rating_tag.text.strip() if rating_tag else None,
                    "rating_count": (
                        int(re.search(r"\d+", rating_count_tag.text.strip()).group())
                        if rating_count_tag
                        else None
                    ),
                    "productId": productId,
                    "itemId": itemId,
                    "vendorItemId": vendorItemId,
                }
            )

    return product_data
