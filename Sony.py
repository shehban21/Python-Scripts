#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selectolax.parser import HTMLParser
import slack
import ssl
import certifi
import os

ssl_context = ssl.create_default_context(cafile=certifi.where())
client = slack.WebClient(token='xoxb-3055584262882-5399917143296-XbBmkM45GDtwffk2yWtATZ4X', ssl=ssl_context)
product = "Sony WH-1000XM5"
target_price = 450

def get_data_with_selenium(store, url, selector):
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        driver.get(url)
        if(store=="Best Buy"):
            time.sleep(5)
        page_source = driver.page_source
        html = HTMLParser(page_source)
        element = html.css_first(selector)

        if element:
            price = element.text().strip()
        else:
            price = "Price not found"

        return {"store": store, "price": price, "url": url}
    finally:
        driver.quit()

def main():
    results = [
        get_data_with_selenium(
            "Amazon",
            "https://www.amazon.ca/dp/B09XS7JWHH",
            "span.a-offscreen"
        ),
        get_data_with_selenium(
            "Best Buy",
            "https://www.bestbuy.ca/en-ca/product/sony-wh-1000xm5-over-ear-noise-cancelling-bluetooth-headphones-black/16162187",
            "span.screenReaderOnly_2mubv",
        ),
        get_data_with_selenium(
            "The Source",
            "https://www.thesource.ca/en-ca/audio-headphones/headphones/noise-cancelling-headphones/sony-wh-1000xm5-wireless-noise-cancelling-over-ear-headphones---silver/p/108100146",
            "div.pdp-sale-price",
        ),
        get_data_with_selenium(
            "The Sony Shop",
            "https://www.thesonyshop.ca/collections/headphones/products/wh1000xm5#",
            "div.price--main span.money",
        ),
        get_data_with_selenium(
            "Staples",
            "https://www.staples.ca/products/3033227-en-sony-wh1000xm5-wireless-noise-cancelling-headphones-black",
            "p.money",
        ),
        get_data_with_selenium(
            "TSC",
            "https://www.tsc.ca/pages/productdetails?nav=R:718627&edp=12956725",
            "div.pdp-description__prices--is-price",
        )
    ]
    for i in results:
        price = i["price"].replace("$","")
        print(price)
        if(float(price) < target_price):
            client.chat_postMessage(channel="C0316UL1JG7", text=" Price of " + product + " is below your target of " + str(target_price) + " and is currently price at: " + str(i["price"]) + " at " + i["store"] + " URL: " + i["url"])

if __name__ == "__main__":
    main()


# In[ ]:




