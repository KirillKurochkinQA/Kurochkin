from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

ENABLE_AFTER = "xpath", "//button[@id='enableAfter']"
VISIBLE_AFTER = "xpath", "//button[@id='visibleAfter']"

wait = WebDriverWait(driver, 10, poll_frequency=1)
driver.get("https://demoqa.com/dynamic-properties")

wait.until(EC.element_to_be_clickable(ENABLE_AFTER))
wait.until(EC.visibility_of_element_located(VISIBLE_AFTER))