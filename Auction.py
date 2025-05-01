#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup

from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

def main():
    lot = input("Enter Lot Number:")
    target_price = int(input("Enter target price:"))
    driver.get('https://www.maxx.ca/Event/LotDetails/' + lot)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    current_price = driver.find_element(By.XPATH,"/html/body/div/div[3]/main/div[2]/div[4]/div/div[2]/div[3]/div[4]/h3/span[2]/span")
    current_price = int(current_price.text)
    total_price = current_price * 1.356
    if (total_price < target_price):
        print(total_price)
    else:
        print("price out of range")


# In[2]:


main()

