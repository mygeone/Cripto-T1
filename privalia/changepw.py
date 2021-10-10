# -*- coding: latin-1 -*-


from selenium import webdriver
from selenium.webdriver.support import wait
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome("./chromedriver_win32/chromedriver")


#declaro variables
email = "myge.one@gmail.com"
pw = "123!@#asdASD"

newPw = '123!@#asdASD'

#get link
driver.get('https://es.privalia.com/authentication/portal/ES')

#fill login 
driver.find_element_by_xpath('/html/body/div[1]/section/div[1]/form/fieldset/p[1]/input').send_keys(email)
driver.find_element_by_xpath('/html/body/div[1]/section/div[1]/form/fieldset/p[2]/input').send_keys(pw)

#click login
driver.find_element_by_xpath('/html/body/div[1]/section/div[1]/form/fieldset/span/input').click()

#redirect account
driver.get('https://es.privalia.com/memberaccount/memberaccount')

#open change pw
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/section[1]/div/div[7]/div[4]').click()


#pw values
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/section[1]/div/div[8]/div/fieldset/div[1]/input').send_keys(pw)
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/section[1]/div/div[8]/div/fieldset/div[2]/input').send_keys(pw)
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/section[1]/div/div[8]/div/fieldset/div[3]/input').send_keys(pw)

time.sleep(2)
#click change
driver.find_element_by_id('#pwdUpdate').click()
