from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome("./chromedriver_win32/chromedriver")

name = 'nameTest'
secondName = 'secondNameTest'
email = 'a2@test.cl'
rut = 191853123
password = 'asdasd'

driver.get('https://www.refreshstore.cl/auth/register')

#fill values
driver.find_element_by_name("nombre").send_keys(name)
driver.find_element_by_name("apellido").send_keys(secondName)
driver.find_element_by_name("email").send_keys(email)
driver.find_element_by_name("rut").send_keys(rut)
time.sleep(3)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_name("confirmar_contraseña").send_keys(password)

#click button
driver.find_element_by_xpath('//*[@id="form-registro"]/button').click()

#driver.close()