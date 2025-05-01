#!/usr/bin/env python
# coding: utf-8

# In[11]:


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

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

def main():
    url = "https://www.tsc.ca/pages/productdetails?nav=R:718627&edp=12956725"
    try:
        driver.get(url)
        page_source = driver.page_source
        html = HTMLParser(page_source)
        element = html.css_first("button.pdp-description__add-to-bag__add-to-bag-button")
        stock_status = element.text().strip() 

        if stock_status != "Out of Stock":
            print("In Stock")
            price_element = html.css_first("div.pdp-description__prices--is-price")
            price = price_element.text().strip()
            price = price.replace("$","")
            if(float(price) < 350):
                client.chat_postMessage(channel="C0316UL1JG7", text="Product is in Stock and the price is $" + price)
        
    finally:
        driver.quit()
        
if __name__ == "__main__":
    main()


# In[ ]:




