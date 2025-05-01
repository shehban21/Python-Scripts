#!/usr/bin/env python
# coding: utf-8

# In[4]:


from bs4 import BeautifulSoup
import slack
import ssl
import certifi
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

ssl_context = ssl.create_default_context(cafile=certifi.where())
client = slack.WebClient(token='xoxb-3055584262882-5399917143296-XbBmkM45GDtwffk2yWtATZ4X', ssl=ssl_context)

def extract_record(item):
    plans = item.find('p').text.strip()
    
    return plans

driver = webdriver.Chrome(ChromeDriverManager(path='https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/115.0.5790.170/mac-arm64/chrome-mac-arm64.zip	').install())

def main():
    driver.get('https://publicmobile.ca/en/on/plans')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    promotions = soup.find_all('div',{'class':'mvne-absolute mvne-bottom-0 mvne-w-full mvne-h-11 mvne-bg-apricot-100 mvne-flex mvne-justify-center mvne-items-center md:mvne-rounded-b-lg font-extrabold medium text-slate-100'})
    
    for item in promotions:
        plan = extract_record(item)
        print(plan)
        client.chat_postMessage(channel="C0316UL1JG7", text=plan)
    driver.close()


# In[ ]:


main()


# In[ ]:




