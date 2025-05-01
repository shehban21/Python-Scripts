#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import slack
import ssl
import certifi
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

ssl_context = ssl.create_default_context(cafile=certifi.where())
client = slack.WebClient(token=os.environ['SLACK_TOKEN'], ssl=ssl_context)

def main():
    driver.get('https://www.denimsociety.com/collections/bauhaus-jackets/products/mens-denim-jacket-with-built-in-hood-black')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    price = soup.find('span',{'id':'ProductPrice-product-template-bauhaus'})
    price_text = price.text.strip()
    price_number = price_text.replace("$","")
    print(price_number)
    if(float(price_number) < 50):
        client.chat_postMessage(channel="C0316UL1JG7", text="The price has dropped to below your desired price of 50 to " + price_text)


# In[2]:


main()


# In[ ]:




