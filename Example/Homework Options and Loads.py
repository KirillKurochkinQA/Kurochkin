import time
from selenium import webdriver

options = webdriver.ChromeOptions()
# options.add_argument("--headless=new")
# options.add_argument("--incognito")
# options.add_argument("--ignore-certificate-errors")
# options.add_argument("--window-size=1920,1080")
# options.add_argument("--disable-cache")

# options.page_load_strategy="normal"
# options.page_load_strategy="eager"

driver = webdriver.Chrome(options=options)
driver.get("https://ya.ru")
print(driver.title)
driver.quit()

driver = webdriver.Chrome()
driver.get("https://demoqa.com/upload-download")
upload_file_field = driver.find_element("xpath", "//input[@id='uploadFile']")
upload_file_field.send_keys(r"C:\Users\kiril\PycharmProjects\Kurochkin\123.jpeg")
download_file_field = driver.find_element("xpath", "//a[@id='downloadButton']")
download_file_field.click()
time.sleep(3)