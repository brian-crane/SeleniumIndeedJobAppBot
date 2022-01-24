import random
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys

from Tools import Tools
delay = 1
driver = Tools()
#driver.get("https://www.indeed.com/?from=gnav-homepage")
time.sleep(delay)

terms = ["QA Engineer Python", "Python Developer",
         "Selenium", "Java Developer",
         "Python Software Developer inTest"]
random.shuffle(terms)

for term in terms:
    urls = driver.get_all_urls(term)
    print("Applying for " + str(len(urls)) + " jobs about " + term)

    random.shuffle(urls)
    for url in urls:
        print("Testing " +url)
        try:
            driver.get(url)
            driver.hit_apply()
            while "viewjob" not in driver.url() and "post-apply" not in driver.url():
                if driver.if_url_contains("questions"):
                    driver.answer_questions()
                elif driver.if_url_contains("documents"):
                    driver.cover_letter_and_recs()
                else:
                    driver.hit_apply()
            driver.hit_apply()
            print("Submitted!")
        except Exception as e:
            driver.handle_error(str(e))
            print("Error processing " + url)

    print("DONE")

driver.kill()