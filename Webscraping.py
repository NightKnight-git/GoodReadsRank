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

for i in range(50):
    time.sleep(10)
    try:
        print("try",i)
        Button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/main/div[2]/div[1]/div[3]/div/div/button/span')))
        Button.click()
    except: 
        try:
            print("except",i)
            Button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div[1]/div')))
            Button.click()
        except:
            break 

       
   
 
    

 
ranking = driver.find_elements_by_css_selector('h2.Text.Text__h2.Text__italic.Text__subdued')

for i in ranking: 
    print(i.text)
