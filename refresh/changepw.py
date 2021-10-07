# -*- coding: latin-1 -*-


from selenium import webdriver
from selenium.webdriver.support import wait
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome("./chromedriver_win32/chromedriver")


#declaro variables
email = 'myge.one@gmail.com'
pw = ''
newPw = 'newPw2'

#get link
driver.get("https://www.refreshstore.cl/auth/login")

#fill login 
driver.find_element_by_name("email").send_keys(email)
driver.find_element_by_name("password").send_keys(pw)

#click login
driver.find_element_by_xpath('//*[@id="form-login"]/div[4]/button').click()

time.sleep(5)
driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/section[2]/form/div[1]/label/input').send_keys(pw)

#new pass debe tener al menos 6 caracteres

#fill values and click
driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[2]/section[2]/form/div[2]/label/input").send_keys(newPw)
driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[2]/section[2]/form/div[4]/label/input").send_keys(newPw)
driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/section[2]/form/div[3]/button').click()
