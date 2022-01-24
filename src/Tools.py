import time

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip

delay = 2
options = Options()
options.add_argument("user-data-dir=C:/Users/brian/AppData/Local/Google/Chrome/User Data - Copy")
driver = webdriver.Chrome(executable_path='C:/Users/brian/Downloads/chromedriver.exe', chrome_options=options)
time.sleep(1)
debug = True

class Tools:
    deadPostCount = 0

    def get(self, url):
        driver.get(url)

    def get_job_postings(self, searchTerm):
        return 0

    def find_element_by_id(self, aid):
        return WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, aid)))

    def find_element_by_xpath(self, xpath):
        return WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))

    def find_element_by_css(self, css):
        return WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))

    def click_apply_button(self):
        #driver.find_element(By.XPATH, "//button[@id='indeedApplyButton']/div").click()
        driver.find_element(By.XPATH, "//button[@id='']").click()

    def get_all_urls(self, term):
        urls = []
        for i in range(0,1):
            driver.get("https://www.indeed.com/jobs?q="+term.replace(" ","%20")+"&l=Sunnyvale%2C%20CA&start="+str(i*10))
            time.sleep(delay)
            links = self.get_all_links()
            for link in links:
                urls.append(link.get_attribute("href"))
        return urls

    def click_continue_button(self):
        driver.find_element(By.XPATH,
                            "//div[@id='ia-container']/div/div/div/main/div[2]/div[2]/div/div/div[2]/div/button/span").click()
        time.sleep(delay)

    def read_file(self,fn):
        text_file = open("C:/Users/brian/IdeaProjects/SeleniumIndeedJobAppBot1/docs/"+fn, "r")
        data = text_file.read()
        text_file.close()
        return data

    def handle_error(self, e):
        self.deadPostCount+=1
        print(str(e))
        time.sleep(delay)
        driver.execute_script("window.open('');")
        time.sleep(delay)
        driver.switch_to.window(driver.window_handles[self.deadPostCount])
        time.sleep(delay)


    def string_to_clipboard(self, text):
        pyperclip.copy(text)

    def write_file(self,fn,text):
        text_file = open("sample.txt", "w")
        n = text_file.write('Welcome to pythonexamples.org')
        text_file.close()

    def cover_letter_and_recs(self):
        text = driver.find_element(By.XPATH, "/html/body").text.lower()

        if "cover letter" in text:
            time.sleep(delay)
            driver.find_element(By.XPATH,"//div[@id='write-cover-letter-selection-card']/div[2]/span").click()
            cover_letter_text = driver.find_element(By.ID,"coverletter-textarea")
            cover_letter_text.click()
            cover_letter_text.send_keys(Keys.CONTROL+"A")
            cover_letter_text.send_keys(Keys.BACKSPACE)
            letter = self.read_file("qa_cover_letter.txt")
            self.string_to_clipboard(letter)
            cover_letter_text.send_keys(Keys.CONTROL+"V")
        if "additional documents" in text:
            additional_docs = driver.find_element(By.ID,"additionalDocuments")
            additional_docs.send_keys("C:/Users/Brian/Downloads/Letters of Recommendation - Brian Crane.pdf")
            time.sleep(delay)
        self.click_continue_button()

    def if_url_contains(self, text):
        if text in str(driver.current_url):
            return True
        return False

    def if_page_contains(self, text):
        time.sleep(delay)
        body = driver.find_element(By.XPATH, "/html/body").text.lower()
        if text.lower() in body:
            return True
        return False

    def answer_questions(self):
        time.sleep(delay)
        text = driver.find_element(By.XPATH, "/html/body").text.lower()
        if "viewjob" in driver.current_url:
            return -1
        elif "answer this question to continue" in text:
            time.sleep(10)
        elif "questions from" in text:
            q_list = text.split("\n")
            answers = []
            for line in q_list:
                if all(x in line for x in ["years", "experience"]):
                    if any(x in line for x in ["quality", "assurance", "qa", "automated",
                                               "java","jira","sql","agile","jenkins",
                                               "junit","testng","test automation",
                                               "rest"]):
                        answers.append("5")
                    elif any(x in line for x in ["python","flask","selenium"]):
                        answers.append("2")
            i = 0
            for number in driver.find_elements(By.XPATH, "//input[@type='number']"):
                number.click()
                number.send_keys(Keys.BACKSPACE)
                number.send_keys(answers[i])
                i += 1
            answers = []
            for line in q_list: #Long form questions
                if any(x in line for x in ["please list 2-3 dates"]):
                    answers.append("Monday or Wednesdays I am available at any time of day.")
                if any(x in line for x in ["require sponsorship"]):
                    answers.append("No.")
            i = 0
            #Text answers
            for text in driver.find_elements(By.TAG_NAME,"textarea"):
                text.click()
                text.send_keys(Keys.BACKSPACE)
                text.send_keys(answers[i])
                i += 1
            #Radio Button questions
            for butt in driver.find_elements(By.XPATH,"//fieldset[@id='input-q_5592f8d2511291e8a7cb1b476b984e4f']/label[2]/span"):
                butt.click()
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
