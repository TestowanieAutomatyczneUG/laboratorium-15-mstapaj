import unittest
from selenium import webdriver

class MyTestCase(unittest.TestCase):
    def test_title(self):
        driver = webdriver.Chrome(executable_path='./chromedriver')
        driver.implicitly_wait(10)
        driver.get("https://duckduckgo.com/")
        driver.find_element_by_id("search_form_input_homepage").send_keys("Selenium")
        driver.find_element_by_id("search_button_homepage").submit()
        self.assertEqual(driver.title, "Selenium at DuckDuckGo")
        driver.quit()


if __name__ == '__main__':
    unittest.main()