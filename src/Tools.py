import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("user-data-dir=C:/Users/brian/AppData/Local/Google/Chrome/User Data - Copy")
driver = webdriver.Chrome(executable_path='C:/Users/brian/Downloads/chromedriver.exe', chrome_options=options)
time.sleep(1)

class Tools:

    def go_to(self, url):
        if "http" not in url:
            url = "https://" + url
            driver.get(url)

    def get_job_postings(self, searchTerm):
        return 0

    def get_element_by_id(self, aid):
        return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, aid)))

    def kill(self):
        driver.close()
