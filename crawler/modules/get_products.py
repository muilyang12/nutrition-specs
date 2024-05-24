import requests
import re

from bs4 import BeautifulSoup

from . import constants


def get_products(searchString: str, headers):
    product_data = []

    url = f"https://www.coupang.com/np/search?q={searchString}"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        products = soup.select(".search-product")

        for product in products:
            a_tag = product.select_one("a")
            name_tag = product.select_one("div.name")
            rating_tag = product.select_one("em.rating")
            rating_count_tag = product.select_one("span.rating-total-count")

            if a_tag:
                href = a_tag.get("href")
                url = (constants.COUPANG_DOMAIN + href.split("?")[0]) if href else None
            else:
                url = None

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
                }
            )

    return product_data
