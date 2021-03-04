from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time

PATH = "/Users/andrewfillenwarth/Desktop/Projects/selenium/chromedriver"

driver = webdriver.Chrome(PATH)

#driver = webdriver.chromedriver(PATH)

driver.get('http://127.0.0.1:8000/')

search = driver.find_element_by_name("username")
search.send_keys("john")
search = driver.find_element_by_name("password")
search.send_keys("krusty69")
search.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit()