from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome("./chromedriver_win32/chromedriver")


mail = 'a1@test.cl'
password = '234@#$sdfGJH'

driver.get('https://es.privalia.com/gr/registration?CountryCodeUser=ES&accessButtonText=Reg%C3%ADstrate')
time.sleep(3)
#fill values
driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/form/div/div[4]/div/div/input').send_keys(mail)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/form/div/div[5]/div/div[1]/div/input').send_keys(password)

time.sleep(3)

#click button
driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/form/div/div[9]/button').click()

driver.close()