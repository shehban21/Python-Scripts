#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import csv
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

def main():
    records = []
    links = []
    driver.get('https://open.spotify.com/playlist/37i9dQZF1DX7iB3RCnBnN4#login')
    time.sleep(2)
    try:
        button = driver.find_element(By.XPATH,'/html/body/div[4]/div/div[3]/div/div[2]/button')
        wait = WebDriverWait(driver, timeout=2)
        wait.until(lambda _ : button.is_displayed())
        if button:
            button.click()
    except Exception:
        pass

    html = driver.find_element(By.TAG_NAME, 'body')
    html.click()
    N = 1
    
    for _ in range(N):
        html.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.5)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        playlist = soup.find_all('div',{'data-testid':'tracklist-row'})
        for track in playlist:
            link = track.find('a', {'data-testid': 'internal-track-link'})
            print(link.get('href'))
            artist = track.find('span',{'class':'e-9800-text encore-text-body-small encore-internal-color-text-subdued UudGCx16EmBkuFPllvss standalone-ellipsis-one-line'})
#             if link and artist:
#                 if(link.text != ''):
            track_data = { "track" : link.text, "artist" : artist.text}
            records.append(track_data)
#                     records = sorted(set(records)) 
    seen = set()
    unique = []
    
    for track in records:
        identifier = tuple(sorted(track.items()))
        if identifier not in seen:
            seen.add(identifier)
            unique.append(track)
    
    print(len(unique))
    print(unique)
#         for item in tracks:
#             track_name = item.text
#             print(track_name)
#             if(track_name != ''):
#                 records.append(track_name)
#     records = sorted(set(records))
#     print(len(records))
#     print(records)
    driver.close()
    with open("current.csv", 'w', newline='',encoding='utf-8') as f:
        writer = csv.writer(f, dialect='excel')
        for element in records:
            writer.writerow([element])
        f.close()


# In[2]:


main()


# In[ ]:




