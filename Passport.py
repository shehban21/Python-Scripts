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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

ssl_context = ssl.create_default_context(cafile=certifi.where())
client = slack.WebClient(token='xoxb-3055584262882-5399917143296-XbBmkM45GDtwffk2yWtATZ4X', ssl=ssl_context)

service = Service()
options = webdriver.ChromeOpitons()
driver = webdriver.Chrome(service=service, options=options)

def main():
    driver.get('https://etatpasseport-passportstatus.service.canada.ca/en/status')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    agree = driver.find_element(By.ID,"btn-agree").click()
    time.sleep(5)
    url = driver.current_url
    driver.get(url)
    soup1 = BeautifulSoup(driver.page_source, 'html.parser')
    agree = driver.find_element(By.ID,"with-esrf").click()
    time.sleep(5)
    url = driver.current_url
    driver.get(url)
    soup1 = BeautifulSoup(driver.page_source, 'html.parser')
    file_number = driver.find_element(By.ID,"esrf")
    file_number.send_keys('3001058579')
    givenName = driver.find_element(By.ID,"givenName")
    givenName.send_keys('Shehban Hashim')
    surname = driver.find_element(By.ID,"surname")
    surname.send_keys('Patel')
    drpyear = Select(driver.find_element(By.ID,"dateOfBirth-year"));
    drpyear.select_by_visible_text("1995");
    drpmonth = Select(driver.find_element(By.ID,"dateOfBirth-month"));
    drpmonth.select_by_visible_text("05");
    drpday = Select(driver.find_element(By.ID,"dateOfBirth-day"));
    drpday.select_by_visible_text("20");
    submit = driver.find_element(By.ID,"btn-submit").click()
    time.sleep(5)
    status_header = driver.find_element(By.XPATH,"/html/body/div/div/main/div[2]/h1")
    status = status_header.get_attribute("data-testid")
    if status == "no-record":
        more_info = driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/ul")
        client.chat_postMessage(channel="C0316UL1JG7", text="Passport Status: " + status + "\n" + status_header.text + " because: " + more_info.text)
    elif status == "being-processed":
        more_info = driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/p[1]")
        client.chat_postMessage(channel="C0316UL1JG7", text="Passport Status: "+ status + "\n" + status_header.text + "\n" + more_info.text)
    elif status == "printed-and-mailed":
        more_info = driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/h1")
        tracking = driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div[2]/section/div/p[2]/a")
        carrier = driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div[2]/section/div/h2")
        tracking_number = driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div[2]/section/div/p[1]")
        client.chat_postMessage(channel="C0316UL1JG7", text="Passport Status: "+ status + "\n" + status_header.text +"\n" + carrier.text + "\n" + tracking_number.text + "\nTracking Link : " + tracking.get_attribute('href'))
    driver.close()


# In[2]:


main()


# In[ ]:




