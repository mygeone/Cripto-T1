from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome("./chromedriver_win32/chromedriver")

username = "a@test.cl"
password = "password"

driver.get("https://www.refreshstore.cl/auth/login")

#fill values
driver.find_element_by_name("email").send_keys(username)
driver.find_element_by_name("password").send_keys(password)

#click button
driver.find_element_by_xpath('//*[@id="form-login"]/div[4]/button').click()