import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):
    def test_links(self):
        driver = webdriver.Chrome(executable_path='./chromedriver')
        driver.implicitly_wait(10)
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[1]').click()
        time.sleep(2)
        links = driver.find_elements(By.XPATH, '//a[@href]')
        self.assertEqual(23, len(links))
        driver.quit()

    def test_images(self):
        driver = webdriver.Chrome(executable_path='./chromedriver')
        driver.implicitly_wait(10)
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[1]').click()
        time.sleep(2)
        images = driver.find_elements(By.XPATH, '//*[@id="react-root"]//img')
        self.assertEqual(7, len(images))
        driver.quit()

    def test_enter_links(self):
        driver = webdriver.Chrome(executable_path='./chromedriver')
        driver.implicitly_wait(10)
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[1]').click()
        time.sleep(2)
        links = driver.find_elements(By.XPATH, '//a[@href]')
        allURLs = []
        for i in range(len(links)):
            driver.find_elements(By.XPATH, '//a[@href]')[i].click()
            time.sleep(1)
            allURLs.append(driver.current_url)
            driver.back()
            if driver.current_url != "https://www.instagram.com/":
                temp = driver.window_handles[1]
                driver.switch_to.window(temp)
                driver.close()
                temp = driver.window_handles[0]
                driver.switch_to.window(temp)
                driver.get("https://www.instagram.com/")
                time.sleep(2)
            time.sleep(1)
        self.assertEqual(len(links), len(allURLs))
        driver.quit()

    def test_form(self):
        driver = webdriver.Chrome(executable_path='./chromedriver')
        driver.implicitly_wait(10)
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[1]').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/article/div[2]/div[2]/div/p/a/span').click()
        time.sleep(2)
        inputs = driver.find_elements(By.XPATH, '//input')
        self.assertEqual(4, len(inputs))
        driver.quit()


if __name__ == '__main__':
    unittest.main()
