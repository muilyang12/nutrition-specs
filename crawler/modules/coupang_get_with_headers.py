import requests

from .constants import COUPANG_HEADERS


def coupang_get_with_headers(url: str):
    return requests.get(url, headers=COUPANG_HEADERS)
