#!/usr/bin/env python
# coding: utf-8

# In[3]:


from bs4 import BeautifulSoup
import slack
import ssl
import certifi
import os
import re
import json
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

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

mydb = client["Cluster0"]
mycol = mydb["Questions"]

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

def main():
    driver.get('https://www.yourlibrary.ca/citizenship-test-answer-keys/')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    test = driver.find_elements(By.XPATH, "//form[@id='citizenship-answers-form']/div/div/label")
    answers = driver.find_elements(By.XPATH, "//form[@id='citizenship-answers-form']/div/div/ul")
    for i, (question, answer) in enumerate(zip(test, answers)):
#         mydict = { "_id" : i , "question" : re.sub('\d+\. ','',question.text) }
#         x = mycol.insert_one(mydict)
        answerOptions = answer.text.replace(' (correct answer)','').split('\n');
        mycol.update_one({"_id" : i } , {"$set" : {"answers":answerOptions}}, True)
#         print(str(i) + "\n" + re.sub('\d+\. ','',question.text) + "\n" + answer.text.replace(' (correct answer)','').split('\n'))
    for i, answer in enumerate(answers):
        no_of_answers = len(answers) -1
        if len(answers) > 0:
            answer = answers[i]
            allanswers = answer.find_elements(By.TAG_NAME, "li")
            for k, xyz in enumerate(allanswers):
                cvb = xyz.find_elements(By.XPATH,"//label/span[@class='correct']")
                for j,bnm in enumerate(cvb):
                    if i != 0 or k != 0:
                        break
                    else:
                        mycol.update_one({"_id" : j } , {"$set" : {"correct_answer":bnm.text.replace(' (correct answer)','')}}, True)
#                         print(j, bnm.text.replace(' (correct answer)',''))
    driver.close()


# In[2]:


main()


# In[ ]:




