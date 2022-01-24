import random
import time

from selenium.webdriver import Keys

from Tools import Tools

driver = Tools()
driver.get("https://www.indeed.com/?from=gnav-homepage")
time.sleep(3)

links = driver.get_all_links()
urls = []
for link in links:
    urls.append(link.get_attribute("href"))
random.shuffle(urls)
for url in urls:
    driver.get(url)
    time.sleep(3)
    driver.click_apply_button()
    time.sleep(1)
    driver.click_continue_button()
    driver.answer_questions()
    driver.click_continue_button() #Past Work Experience


    time.sleep(3)


time.sleep(30)

driver.kill()