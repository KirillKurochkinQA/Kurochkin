import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")
page_url = driver.current_url
print(page_url)
assert page_url == "https://www.saucedemo.com/", "Адрес URL изменен"
page_title = driver.title
print(page_title)
assert page_title == "Swag Labs", "Title изменен"
driver.quit()

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
page_title = driver.title
assert page_title == "Swag Labs", "Title изменен"
print("Тест на проверку Title прошел успешно")
driver.quit()

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
assert len(driver.find_elements("xpath", "//input[@data-test='username']")) == 1, f"Неверное количество полей ввода логина: {len(driver.find_elements("xpath", "//input[@data-test='username']"))}"
print("Тест на проверку наличия поля ввода логина прошел успешно")
driver.quit()