COUPANG_DOMAIN = "https://www.coupang.com"

CURL_COMMAND = """
curl "https://www.coupang.com/" ^
  -H "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7" ^
  -H "accept-language: ko" ^
  -H "cache-control: no-cache" ^
  -H ^"cookie: sid=2b22421c3e394e768395bbe7b3038bdbecc99302; PCID=1356487393829617028094; overrideAbTestGroup=^%^5B^%^5D; MARKETID=1356487393829617028094; x-coupang-accept-language=ko-KR; x-coupang-target-market=KR; bm_sz=BA565CE94C791740BC371237D2370270~YAAQTQI1F8jw+qSPAQAABf9AqhcFFrJAWdnw69bbu0VjkyNjdUWqAgOXSDsMpVX2aRKC+5Dlr4QzT16Z313dI2wQ7AiAsVIl9BsSfMIAyLbuFIzqO02lAJu56iqZ1rvpg98BJb1f/wdsE510Ax3SQ7aBUE4aWWS0D4qd3Ka8QnNmZn8DywFD2MtkJ5+ZxxX2E+5fSmvrZ5jVDKdZQ7uW6PgMMYpuJUmuN435Tw3pPs7kCdhKEJiJ0VmELEIKxV4agdYg/mqjm5wbNrXfLXH9K3p0IM9OHUEvSCbk2hSpnyTpDhB37iaTGOF9jh9O39AvNnwFwk8QvBk7seDO7FFvBeM6qP/sKPkEHw23lqljSNwZ+B62Howen1xlKzG73BOWHHoSzWUvfq/2nc1VH30=~3686964~4343106; _fbp=fb.1.1716548338608.2048951147; cto_bundle=KNOlql9lRGtUcmR3c1RYeEZLazkzeE55ejFNNUM4RHM5TldnRkQlMkJLemdzejVZQWJmRVBrYmpTZktjWjlOZWQ1eDdhRnFUJTJCYzF0b3o2bDFvTW8yMCUyQlRDeVdhcnhyWkN6M1lZeDBDTmJSZ2J1QlpJak8zNWp1JTJGak02N2g0cHEyZkQ5dmF6; baby-isWide=small; ak_bmsc=242ABFD2F9ED5E1A88B0E7E5C6A8D093~000000000000000000000000000000~YAAQTQI1Fx/y+qSPAQAAKwRBqhec3sCDZZk8ZpEgH7J4Qy/AXltjdDTjfuIUrrAAhxAjKL6ZYCVgAVtIDCJ4nH2u8tDgGd8HqPzbuCOTCp2xVwhTdusbhh8mUtC4Q5reZ/4S55Z2AP60y63MvjPgY41jXuqdnoUm+JAPyZ/DIQSJTFTGlHfNFEk42FNlOVi0CTxbTHhJH8wcUvTlDGOWn0egNrT4CFjx79x+8Ws3D3C+mZzo8HKnAnpMuhnb1rpxNRSHTaPHv06IZiU+0b9jX/Y2lzdXdw2Az+rGNrRSYo+rNkP1xNjl9cYxipnl0QCV5HKCybWYpJ1BwztpdHnxwwE9CUAWtz9wOgDQz4QsohgO4Q9eSNVIry4/mbdQfiYW8BEuOAEJGCae1YIpSOzb58+TqCUW+e+dVDTOYQrev/qbW94yDtPeO2c/WTxT9vlQMw3+tat+lCI8vbR8y+k=; bm_sv=820B84A0F90C9C9F49EFEC53A7546E57~YAAQTQI1F7jy+qSPAQAAWwZBqherMoyl0r+ACU7FfsMpOvm1D/aMpNxT/JDDABZ5NQeecKXIdqrdHm0A2cb26EezvB/QqwjjoTY9tz07S3qk2ir0ZPNIajeJBVSjTZ1GoFa1JNx3xyo0puwAdHdLKLemOuoMoW0ExQNld989MdQBFObyQ7YmyGac0belrdXrxQIfIpVqXh8xCf0Egqn9C5ABp4DbzBWBh9C0TsGpMHUSJkWJPJLEDZs4Q1GQDQWkEg==~1; _abck=E7ACCF8C0331D83DD7E894D934D6F0E3~-1~YAAQX2qituKPYKSPAQAAlQ9FqgtKpTXGAoqdRm/bIooLaPvyDj6FXluQ1/tJMQQ3AZhSKbLdOizRyfoJttwk0ypz5Cf0G7tRbF3NDHoDcoL4PrFmoys5vlmaYjN3ODyWoEnnOxNK7vBbG7bMa7OlY7LsvnjEP0RVl1qTtEOOlDBlKehklpRt9BBmJ7HXgrbqtM/frvvdbRddmNrdhykN4k7SrFe/TMg/YwN1aRQH5Ns7WNsgsk/dknAM8MbgNdtsjIbXaWUkuNmUUMyOUWqV74zKjbfN/JwG74eJAXk0MWXv5I/R3nj6XmX/6s9M0QJ5Z96HCoVXcpB/36E9r0G6aWcRFIm3/bo3Un7/wAVP3JQ66qAXTibUQEn/XyxLWUI+XXpIiRYj1yY4SPE=~-1~^|^|0^|^|~-1^" ^
  -H "pragma: no-cache" ^
  -H "priority: u=0, i" ^
  -H ^"sec-ch-ua: ^\^"Google Chrome^\^";v=^\^"125^\^", ^\^"Chromium^\^";v=^\^"125^\^", ^\^"Not.A/Brand^\^";v=^\^"24^\^"^" ^
  -H "sec-ch-ua-mobile: ?0" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" ^
  -H "sec-fetch-dest: document" ^
  -H "sec-fetch-mode: navigate" ^
  -H "sec-fetch-site: none" ^
  -H "sec-fetch-user: ?1" ^
  -H "upgrade-insecure-requests: 1" ^
  -H "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
"""
