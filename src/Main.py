import time

from selenium.webdriver import Keys

from Tools import Tools

myTools = Tools()
myTools.go_to("indeed.com")

searchBar = myTools.get_element_by_id("text-input-what")
searchBar.click()
searchBar.send_keys("QA Engineer")
searchBar.send_keys(Keys.ENTER)

time.sleep(5)

myTools.kill()

print("Goodbye")