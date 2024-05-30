import re

from bs4 import BeautifulSoup

from . import constants
from .coupang_get_with_headers import coupang_get_with_headers


def get_products(search_tring: str):
    product_data = []

    response = coupang_get_with_headers(
        f"https://www.coupang.com/np/search?q={search_tring}"
    )

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        products = soup.select(".search-product")[:3]

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

            product_data.append(
                {
                    "url": url,
                    "name": name_tag.text.strip() if name_tag else None,
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
