from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome("./chromedriver_win32/chromedriver")

username = "a@test.cl"
password = "password"

driver.get('https://es.privalia.com/authentication/')


time.sleep(3)

driver.find_element_by_xpath('/html/body/div[1]/section/div[1]/form/fieldset/p[1]/input').send_keys(username)
driver.find_element_by_xpath('/html/body/div[1]/section/div[1]/form/fieldset/p[2]/input').send_keys(password)

driver.find_element_by_xpath('/html/body/div[1]/section/div[1]/form/fieldset/span/input').click()

