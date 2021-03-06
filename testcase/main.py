import unittest
from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):

    def setup(self):
        self.driver = webdriver.Chrome("/Users/andrewfillenwarth/Desktop/Projects/selenium/chromedriver")
        self.driver.get("http://www.python.org")
    
    def test_title(self):
        mainPage = page.MainPage()
        assert mainPage.is_title_matches()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()