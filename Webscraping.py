"""
This file is used to webscrape the top books from the year 2021 on the GoodReads sight
using selenium
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time 

driver = webdriver.Chrome('/Users/reaganolguin/Downloads/chromedriver')
driver.get('https://www.goodreads.com/book/popular_by_date/2021')


time.sleep(5)

# Setting up the page so that all the top books included in 2021 can be scraped 
#Pressing the "load more books" button as many times as needed
while True:
    time.sleep(10)
    try:
        Button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/main/div[2]/div[1]/div[3]/div/div/button/span')))
        Button.click()
    except: 
        try:
            Button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div[1]/div')))
            Button.click()
        except:
            break 

# grabbing all the rankings of each book
ranking = driver.find_elements_by_css_selector('h2.Text.Text__h2.Text__italic.Text__subdued')
ranking_list = [i.text for i in ranking]
print(ranking_list)

