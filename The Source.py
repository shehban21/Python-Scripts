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

def get_data_with_selenium(url):
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        driver.get(url)
        product_name = ""
        page_source = driver.page_source
        html = HTMLParser(page_source)
        element = html.css_first("div.pdp-sale-price")
        name = html.css_first("h1.pdp-name")

        if element:
            price = element.text().strip()
        else:
            price = "Price not found"
        if name:
            product_name = name.text().strip()
        else:
            price = "Price not found"

        return {"name": product_name, "price": price, "url":url}
    finally:
        driver.quit()

def main():
    target_price = 100;
    results = [
       get_data_with_selenium("https://www.thesource.ca/en-ca/gaming/xbox/all-xbox-series-x-s-/thrustmaster-t128-x-racing-wheel-for-xbox%c2%ae-series-x-s%2c-xbox-one-and-pc/p/108102766?itemListName=Clearance+%7c+Clearance+%7c+The+Source")
    ]
    for i in results:
        price = i["price"].replace("$","")
        name = i["name"]
        if(float(price) < target_price):
            client.chat_postMessage(channel="C0316UL1JG7", text="the source price matches target")
        else:
            print(name, price)

if __name__ == "__main__":
    main()

