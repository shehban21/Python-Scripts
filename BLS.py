#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import slack
import ssl
import json
import time
import certifi
import os
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

ssl_context = ssl.create_default_context(cafile=certifi.where())
client = slack.WebClient(token='xoxb-3055584262882-5399917143296-XbBmkM45GDtwffk2yWtATZ4X', ssl=ssl_context)

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

def main():
    driver.get('https://www.blsindia-canada.com/appointmentbls/appointment.php')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    location = Select(driver.find_element(By.XPATH,"/html/body/div[2]/section[1]/div/div[3]/div[1]/table/tbody/tr[2]/td/table/tbody/tr[6]/td[2]/select"))
    location.select_by_visible_text('Brampton')
    service = Select(driver.find_element(By.XPATH,"/html/body/div[2]/section[1]/div/div[3]/div[1]/table/tbody/tr[2]/td/table/tbody/tr[7]/td[2]/select"))
    service.select_by_visible_text('Visa')
    available_date = driver.find_element(By.XPATH,"/html/body/div[2]/section[1]/div/div[3]/div[1]/table/tbody/tr[2]/td/table/tbody/tr[8]/td[2]/input")
    driver.execute_script("arguments[0].removeAttribute('readonly',0);", available_date)
    available_date.send_keys('2024-06-28')
    time.sleep(10)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    slot = driver.find_element(By.ID,"app-slot")
    print(driver.page_source.encode('utf-8'))
    available_slot = driver.find_element(By.ID,"app-slot")
#     try:
#         available_slot = driver.find_element(By.XPATH,"/html/body/div[2]/section[1]/div/div[3]/div[1]/table/tbody/tr[2]/td/table/tbody/tr[9]/td[2]/select")
#         print("slot available")
#     except NoSuchElementException:
#         print("slot not available")
#     print(available_slot)
#     driver.close()
    # /html/body/div[2]/section[1]/div/div[3]/div[1]/table/tbody/tr[2]/td/table/tbody/tr[9]/td[2]/select


# In[2]:


main()


# In[ ]:




