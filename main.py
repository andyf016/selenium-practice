from selenium import webdriver 
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time



PATH = "/Users/andrewfillenwarth/Desktop/Projects/selenium/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get('https://orteil.dashnet.org/cookieclicker')
driver.implicitly_wait(5)

actions = ActionChains(driver)
