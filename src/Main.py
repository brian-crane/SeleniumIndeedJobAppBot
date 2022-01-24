import random
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys

from Tools import Tools
delay = 3
driver = Tools()
#driver.get("https://www.indeed.com/?from=gnav-homepage")
time.sleep(delay)

terms = ["QA Engineer Python"]
for term in terms:
    urls = driver.get_all_urls(term)
    print("Applying for " + str(len(urls)) + " jobs about " + term)

    random.shuffle(urls)
    for url in urls:
        try:
            driver.get(url)
            time.sleep(delay)
            driver.click_apply_button()
            time.sleep(delay)
            while driver.if_url_contains("review") is False:
                if driver.if_url_contains("questions"):
                    driver.answer_questions()
                elif driver.if_url_contains("documents"):
                    driver.cover_letter_and_recs()
                else:
                    driver.click_continue_button()
            driver.click_continue_button()
            print("Submitted!")
        except Exception as e:
            driver.handle_error(str(e))
            print("Error processing " + url)

    print("DONE")

driver.kill()