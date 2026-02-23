import time
from selenium import webdriver
#DEMOQA
driver = webdriver.Chrome()

site = "https://demoqa.com/text-box"
driver.get(site)

full_name_field = driver.find_element("xpath","//input[@id='userName']")
full_name_field.clear()
assert full_name_field.get_attribute("value") == ""
full_name_field.send_keys("Kirill")
assert full_name_field.get_attribute("value") == "Kirill"

email_field = driver.find_element("xpath","//input[@id='userEmail']")
email_field.clear()
assert email_field.get_attribute("value") == ""
email_field.send_keys("kirill@mail.ru")
assert email_field.get_attribute("value") == "kirill@mail.ru"

current_address_field = driver.find_element("xpath","//textarea[@id='currentAddress']")
current_address_field.clear()
assert current_address_field.get_attribute("value") == ""
current_address_field.send_keys("Moscow")
assert current_address_field.get_attribute("value") == "Moscow"

permanent_address_field = driver.find_element("xpath","//textarea[@id='permanentAddress']")
permanent_address_field.clear()
assert permanent_address_field.get_attribute("value") == ""
permanent_address_field.send_keys("Moscow region")
assert permanent_address_field.get_attribute("value") == "Moscow region"
driver.quit()

from selenium.webdriver import Keys
#KEY-PRESSES
driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/key_presses")
INPUT_FIELD = ("xpath","//input[@id='target']")
driver.find_element(*INPUT_FIELD).clear()
assert driver.find_element(*INPUT_FIELD).get_attribute("value") == ""
driver.find_element(*INPUT_FIELD).send_keys("kirill")
assert driver.find_element(*INPUT_FIELD).get_attribute("value") == "kirill"
driver.find_element(*INPUT_FIELD).send_keys(Keys.CONTROL + "A")
time.sleep(5)
driver.find_element(*INPUT_FIELD).send_keys(Keys.BACKSPACE)
time.sleep(5)
assert driver.find_element(*INPUT_FIELD).get_attribute("value") == ""