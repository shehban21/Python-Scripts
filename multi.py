#!/usr/bin/env python
# coding: utf-8

# In[9]:


import httpx
from selectolax.parser import HTMLParser


def get_data(store, url, selector):
    resp = httpx.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:106.0) Gecko/20100101 Firefox/106.0"
        },
    )
    html = HTMLParser(resp.text)
    price = html.css_first(selector).text().strip()
    return {"store": store, "price": price}


def main():
    results = [
        get_data(
            "Amazon",
            "https://www.amazon.ca/dp/B09XS7JWHH/",
            "span.a-offscreen"
        ),
        get_data(
            "Best Buy",
            "https://www.bestbuy.ca/en-ca/product/sony-wh-1000xm5-over-ear-noise-cancelling-bluetooth-headphones-black/16162187",
            "div.price_2j8lL",
        ),
    ]
    print(results)


if __name__ == "__main__":
    main()


# In[ ]:




