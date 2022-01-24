import random
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys

from Tools import Tools
delay = 2
driver = Tools()
driver.get("https://www.indeed.com/?from=gnav-homepage")
time.sleep(delay)

links = driver.get_all_links()
urls = []
for link in links:
    urls.append(link.get_attribute("href"))
random.shuffle(urls)
for url in urls:
    try:
        driver.get(url)
        time.sleep(delay)
        driver.click_apply_button()
        time.sleep(delay)
        while driver.if_page_contains("application step"):
            if driver.if_page_contains("questions from"):
                driver.answer_questions()
            elif driver.if_page_contains("supporting documents"):
                driver.cover_letter_and_recs()
            else:
                driver.click_continue_button()
    except NoSuchElementException as e:
        driver.handle_error(str(e))

time.sleep(30)

driver.kill()