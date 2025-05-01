#!/usr/bin/env python
# coding: utf-8

# In[5]:


import re
import csv
from datetime import datetime
from collections import Counter
import ssl
import slack
import certifi

#minimum count of suspicious activity from a single ip address
minimum_count = 5
#regex to match ip addresses
pattern = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
#list of suspicious ip addresses
sus_ips = []
#today's date
today = datetime.today().strftime('%Y-%m-%d')
#connecting to slack. put your slack server's token here
ssl_context = ssl.create_default_context(cafile=certifi.where())
client = slack.WebClient(token='xoxb-3055584262882-5399917143296-XbBmkM45GDtwffk2yWtATZ4X', ssl=ssl_context)

#opening our log file and analysing with our regex
for i, line in enumerate(open('/Users/shehb/Desktop/Shared/logs/log_anomalies.txt')):
	for match in re.finditer(pattern,line):
		sus_ips.append(match.group())

#counting number of times an ip appeared and filtering low counts
ip_counts = Counter(sus_ips)
ip_counts.most_common()
high_counts = [(x,count) for x, count in ip_counts.items() if count > minimum_count]

#writing to csv file the ip address, number of errors caused by it and the day it happened
for item in high_counts:
	with open('ips.csv', 'a',  newline ='') as csvfile:
		ipwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		ipwriter.writerow([item[0],item[1],today])

#if high counts exists, it means there has been suspicious activity. So message is sent via Slack. Channel ID is required here
if high_counts:
	client.chat_postMessage(channel="C0316UL1JG7",text="Suspicious IP Address Activity Found")


# In[ ]:




