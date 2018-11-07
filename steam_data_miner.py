from html.parser import HTMLParser
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import os



def setup():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_driver = os.getcwd() + '\\chromedriver.exe'
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)
    wait = WebDriverWait(driver, 10)
    driver.get('https://steamcommunity.com/search/users')
    search = driver.find_element_by_class_name('community_search_text_box')
    ActionChains(driver).move_to_element(search).send_keys('c').key_down(Keys.RETURN).key_up(Keys.RETURN).perform()
    driver.implicitly_wait(30)
    results = driver.find_elements_by_class_name('searchPersonaName')
    for x in results:
        link = x.get_attribute('href')
        print(link)
    driver.quit()




def findDiv():
    page = requests.get('https://steamcommunity.com/id/mrk3gs/friends/')
    soup = BeautifulSoup(page.content, 'html.parser')
    divs = soup.findAll('div', {'class': 'friend_block_content'})
    for profile in divs:
        print(profile.contents[0])


setup()
