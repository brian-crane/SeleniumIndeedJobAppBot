import os
import random
import sys
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys

from Tools import Tools
delay = 1
driver = Tools()
#driver.get("https://www.indeed.com/?from=gnav-homepage")
time.sleep(delay)

terms = ["Daily"]
random.shuffle(terms)

for term in terms:
    urls = driver.get_all_urls(term,1,2,3)
    print("Applying for " + str(len(urls)) + " jobs about " + term)
    #random.shuffle(urls)
    for url in urls:
        print("Applying for " +url)
        try:
            driver.get(url)
            answer = input("Do you want to apply to this job? Hit Enter for yes, anything else for no\n")
            if answer in ["y","yes",""]:
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
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            driver.handle_error(str(e))
            print("Error processing " + url)

    print("DONE")

driver.kill()