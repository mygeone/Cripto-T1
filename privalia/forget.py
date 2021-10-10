# -*- coding: latin-1 -*-
from selenium import webdriver
from selenium.webdriver.support import wait
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome("./chromedriver_win32/chromedriver")



email = 'test011@test011.com'
driver.get('https://es.privalia.com/authentication/Login/RecoverPassword')


#ingreso mail
driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/section/div/div/form/fieldset/div/input').send_keys(email)

#click boton
driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/section/div/div/form/div/input').click()
