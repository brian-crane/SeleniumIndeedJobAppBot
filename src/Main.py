from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("user-data-dir=C:/Users/brian/AppData/Local/Google/Chrome/User Data - Copy")
driver = webdriver.Chrome(executable_path='C:/Users/brian/Downloads/chromedriver.exe', chrome_options=options)

driver.get("https://www.indeed.com/")
driver.find_element(By.ID, "text-input-what").click()
driver.find_element(By.ID, "text-input-what").send_keys("test")
driver.close()
