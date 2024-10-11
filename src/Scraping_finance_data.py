from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import datetime
import logging

logging.basicConfig(filename='app.log', filemode='w',level=logging.INFO, format= '%(asctime)s - %(levelname)s - %(message)s - %(lineno)d')

def webdriver_connection():
    '''
    Keep your chromedriver file path in project folder and can manully change executable path,
    according to your chromedriver file path.
    '''
    try:
        service =   Service(executable_path = "/chromedriver")
        driver = webdriver.Chrome(service=service)
    except Exception as e:
        logging.critical(e)
    else:
        driver.maximize_window()
    return driver

def main_site_opening(driver):
    '''This function will request driver for opening website you want to scrap'''
    website = "https://finance.yahoo.com/lookup"
    try:
        driver.set_page_load_timeout(100)
        driver.implicitly_wait(50)
        driver.get(website)
    except Exception as e:
        logging.critical(e)

