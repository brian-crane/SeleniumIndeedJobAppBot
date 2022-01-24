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
for url in urls:
    driver.get(url)
    driver.click_apply_button()
    time.sleep(1)
    driver.click_continue_button()
    butts = driver.get_all_buttons()
    driver.click_continue_button()


time.sleep(30)

driver.kill()