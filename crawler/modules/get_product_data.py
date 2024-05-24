from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import re


def get_product_data(driver, searchString: str):
    product_data = []

    driver.get(
        f"https://www.coupang.com/np/search?component=&q={searchString}&channel=user"
    )

    wait = WebDriverWait(driver, 10)

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".search-product")))

    products = driver.find_elements(By.CSS_SELECTOR, ".search-product")

    for product in products:
        try:
            a_tag = product.find_element(By.TAG_NAME, "a")
            name_tag = product.find_element(By.CSS_SELECTOR, "div.name")
            rating_tag = product.find_element(By.CSS_SELECTOR, "em.rating")
            rating_count_tag = product.find_element(
                By.CSS_SELECTOR, "span.rating-total-count"
            )

            href = a_tag.get_attribute("href")
            url = href.split("?")[0]

            product_data.append(
                {
                    "url": url,
                    "name": name_tag.text,
                    "rating": rating_tag.text,
                    "rating_count": int(
                        re.search(r"\d+", rating_count_tag.text).group()
                    ),
                }
            )

        except:
            continue

    return product_data
