"""
This code is used to webscrape the top books from the year 2021 on the GoodReads sight
using selenium
"""

from os import sep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time 
import re
import pandas as pd 
import numpy as np 

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
rankings = driver.find_elements_by_css_selector('h2.Text.Text__h2.Text__italic.Text__subdued')
rankings_list = [i.text for i in rankings]

# grabbing all of the titles
titles = driver.find_elements_by_css_selector('h3.Text.Text__title3.Text__umber')
titles_list = [i.text for i in titles]

# grabbing all of the authors
authors = driver.find_elements_by_css_selector('div.BookListItem__authors')
authors_list = [i.text for i in authors]
cleaned_authors =[]
for i in authors_list:
    cleaned_string = re.sub(r'\n', '', i)
    cleaned_string = re.sub(r"...more", '',cleaned_string)
    cleaned_authors.append(cleaned_string)





# grabbing all of the book ratings, # of ratings, and the # of shelvings
# This will need to be cleaned later
ratings_and_shelvings = driver.find_elements_by_css_selector('div.BookListItemRating__column.BookListItemRating__column--secondary')
ratings_and_shelvings_list = [i.text for i in ratings_and_shelvings]

# separating the ratings and shelving info into their own individual lists 
rating_list =[]
num_ratings_list = []
num_shelvings_list = []
for i in ratings_and_shelvings_list:
    separated_string = i.splitlines()
    rating_list.append(separated_string[0])
    num_ratings_list.append(separated_string[1])
    num_shelvings_list.append(separated_string[2])



# grab all of the book descriptions
description = driver.find_elements_by_css_selector('div.TruncatedText')
description_list = [i.text for i in description]
# Clean all of the descriptions 
clean_desc_list = []
for i in description_list:
    cleaned_string = re.sub(r'\n', '', i)
    cleaned_string = re.sub(r"\'", "'", cleaned_string)
    clean_desc_list.append(cleaned_string)


# creating the dataframe to be used for analysis 
Books = pd.DataFrame()
Books["Rank"] = rankings_list
Books["Title"] = titles_list
Books["Author"] = cleaned_authors
Books["Rating"] = rating_list
Books["NumberOfRatings"] = num_ratings_list
Books["NumberOfShelves"] = num_shelvings_list
Books["Description"] = clean_desc_list

print(Books) 

