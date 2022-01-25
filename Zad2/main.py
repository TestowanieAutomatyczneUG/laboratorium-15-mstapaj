import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class MyTestCase(unittest.TestCase):
    def test_by_tag_name(self):
        driver = webdriver.Chrome(executable_path='./chromedriver')
        driver.implicitly_wait(20)
        driver.get("https://duckduckgo.com")
        driver.find_element(By.ID, "search_form_input_homepage").send_keys("Selenium")
        driver.find_element(By.ID, "search_button_homepage").submit()
        time.sleep(2)
        driver.find_elements(By.TAG_NAME, 'a')[41].click()
        time.sleep(2)
        self.assertEqual(driver.current_url, 'https://www.selenium.dev/')
        driver.back()
        driver.find_elements(By.TAG_NAME, 'a')[53].click()
        time.sleep(4)
        self.assertEqual(driver.current_url, 'https://ods.od.nih.gov/factsheets/selenium-healthprofessional/')
        driver.quit()

    def test_by_class(self):
        driver = webdriver.Chrome(executable_path='./chromedriver')
        driver.implicitly_wait(20)
        driver.get("https://duckduckgo.com")
        driver.find_element(By.ID, "search_form_input_homepage").send_keys("Selenium")
        driver.find_element(By.ID, "search_button_homepage").submit()
        time.sleep(2)
        print(driver.find_elements(By.CLASS_NAME, 'result__a js-result-title-link'))
        driver.find_elements(By.CLASS_NAME, 'result__a js-result-title-link')[0].click()
        time.sleep(2)
        self.assertEqual(driver.current_url, 'https://www.selenium.dev/')
        driver.back()
        driver.find_elements(By.CLASS_NAME, 'result__a js-result-title-link')[2].click()
        time.sleep(4)
        self.assertEqual(driver.current_url, 'https://ods.od.nih.gov/factsheets/selenium-healthprofessional/')
        driver.quit()

    def test_by_link_text(self):
        driver = webdriver.Chrome(executable_path='./chromedriver')
        driver.implicitly_wait(20)
        driver.get("https://duckduckgo.com")
        driver.find_element(By.ID, "search_form_input_homepage").send_keys("Selenium")
        driver.find_element(By.ID, "search_button_homepage").submit()
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, 'Selenium').click()
        time.sleep(2)
        self.assertEqual(driver.current_url, 'https://en.wikipedia.org/wiki/Selenium')
        driver.back()
        driver.find_element(By.LINK_TEXT, 'Selenium - Health Professional Fact Sheet').click()
        time.sleep(4)
        self.assertEqual(driver.current_url, 'https://ods.od.nih.gov/factsheets/selenium-healthprofessional/')
        driver.quit()

    def test_by_keys_enter_return(self):
        driver = webdriver.Chrome(executable_path='./chromedriver')
        driver.implicitly_wait(20)
        driver.get("https://duckduckgo.com")
        driver.find_element(By.ID, "search_form_input_homepage").send_keys("Selenium")
        driver.find_element(By.ID, "search_button_homepage").submit()
        time.sleep(2)
        driver.find_elements(By.TAG_NAME, 'a')[41].send_keys(Keys.RETURN)
        time.sleep(2)
        self.assertEqual(driver.current_url, 'https://www.selenium.dev/')
        driver.back()
        driver.find_elements(By.TAG_NAME, 'a')[53].send_keys(Keys.ENTER)
        time.sleep(4)
        self.assertEqual(driver.current_url, 'https://ods.od.nih.gov/factsheets/selenium-healthprofessional/')
        driver.quit()


if __name__ == '__main__':
    unittest.main()
