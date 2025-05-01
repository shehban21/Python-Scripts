#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import slack
import ssl
import certifi
import os
import re
import time
import json
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime, timezone
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


uri = "mongodb+srv://shehban:Xtg4SaflKQQgorPB@cluster0.y6jsixk.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = pymongo.MongoClient(uri, tlsCAFile=certifi.where())
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

mydb = client["aeroplan"]
mycol = mydb["aeroplan"]

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

def get_url():
    url = 'https://aeroplan.rewardops.com/en-CA/home/brands?'
    url += 'apiPage={}'
    
    return url

def extract_record(item):
    points = item.find('h3',{'class':'MuiBox-root'}).text.strip()
    
    return points

def main():
    records = []
    url = get_url()
    stores = []
    today = datetime.now(timezone.utc)
        
    for page in range(1,10):
        driver.get(url.format(page))
        time.sleep(15)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        nonfeatured = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/main/section/div/div[3]/div/div[2]/div[2]/section/div")
        search = nonfeatured.find_elements(By.TAG_NAME, "h3")
        
        for item in search:
            print(item.text.strip())
    print(today)
    
#     for item in records:
#         s = item
#         s_str = s.split()
#         if(s_str[0] != "Earn"):
#            continue 
#         keyword = "on "
#         before_keyword, keyword, after_keyword = s.partition(keyword)
#         store_name = after_keyword
#         if store_name not in stores:
#             if(s_str[1] == "up"):
#                 stores.append(store_name)
#                 store_pt = s_str[1] + " " + s_str[2]+ " " + s_str[3]
#                 points = {"date": today, "multiplier": store_pt, "store":store_name}
#                 mycol.insert_one(points)
#                 print(points)
#             else:
#                 stores.append(store_name)
#                 store_pt = s_str[1]
#                 points = {"date": today, "multiplier": store_pt, "store":store_name}
#                 mycol.insert_one(points)
#                 print(points)
#         else:
#             continue
    driver.close()                   


# In[2]:


main()


# In[ ]:




