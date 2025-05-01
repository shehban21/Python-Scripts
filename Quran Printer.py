#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import base64

# Set Chrome options
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode
options.add_argument('--disable-gpu')

# Initialize the WebDriver
driver = webdriver.Chrome(options=options)

def generate_url(i):
    url = "https://quran411.com/print?s=" + str(i)
    print(url)
    return url

# Open the webpage
for i in range(1,115):
    driver.get(generate_url(i))

# Save page as PDF
    pdf_data = driver.execute_cdp_cmd("Page.printToPDF", {
        "landscape": False,
        "displayHeaderFooter": False,
        "printBackground": True,
        "preferCSSPageSize": True
    })

# Decode base64 PDF data and save to file
    pdf_bytes = base64.b64decode(pdf_data['data'])
    with open("/Users/shehb/Desktop/Quran/" + str(i) + ".pdf", "wb") as f:
        f.write(pdf_bytes)

# Close the browser

    print("PDF saved as output.pdf")
driver.quit()


# In[ ]:




