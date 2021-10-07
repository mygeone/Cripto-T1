# -*- coding: latin-1 -*-


from selenium import webdriver
from selenium.webdriver.support import wait
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome("./chromedriver_win32/chromedriver")



email = 'myge.one@gmail.com'
pw = 'newPw1'
newPw = 'newPw2'

driver.get("https://www.refreshstore.cl/auth/resetPassword")

#ingreso mail
driver.find_element_by_xpath('/html/body/div[5]/div/div/section/div/form/div[1]/label/input').send_keys(email)

#click boton
driver.find_element_by_xpath('/html/body/div[5]/div/div/section/div/form/div[2]/button').click()
