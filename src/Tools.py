import time

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("user-data-dir=C:/Users/brian/AppData/Local/Google/Chrome/User Data - Copy")
driver = webdriver.Chrome(executable_path='C:/Users/brian/Downloads/chromedriver.exe', chrome_options=options)
time.sleep(1)
debug = True


class Tools:

    def get(self, url):
        driver.get(url)

    def get_job_postings(self, searchTerm):
        return 0

    def find_element_by_id(self, aid):
        return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, aid)))

    def find_element_by_xpath(self, xpath):
        return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))

    def find_element_by_css(self, css):
        return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))

    def click_apply_button(self):
        driver.find_element(By.XPATH, "//button[@id='']").click()

    def click_continue_button(self):
        driver.find_element(By.XPATH,
                            "//div[@id='ia-container']/div/div/div/main/div[2]/div[2]/div/div/div[2]/div/button/span").click()

    def answer_questions(self):
        text = driver.find_element(By.XPATH, "/html/body").text
        if "Questions from the employer" in text:
            q_list = text.lower().split("\n")
            answers = []
            for line in q_list:
                if all(x in line for x in ["years", "experience"]):
                    if any(x in line for x in ["quality", "assurance", "qa", "automated",
                                               "java","jira","sql","agile","jenkins",
                                               "junit","testng"]):
                        answers.append("5")
                    elif any(x in line for x in ["python","flask"]):
                        answers.append("2")
            i = 0
            for text in driver.find_elements(By.XPATH, "//input[@type='number']"):
                text.click()
                text.send_keys(Keys.BACKSPACE)
                text.send_keys(answers[i])
                i += 1
        else:
            return -1
        self.click_continue_button()
        self.answer_questions()

    def get_all_links(self):
        links = []
        for link in driver.find_elements(By.TAG_NAME, "a"):
            try:
                if "Apply with your Indeed Resume" in link.text:
                    links.append(link)
            except StaleElementReferenceException:
                print("error")
        return links

    def kill(self):
        driver.close()
