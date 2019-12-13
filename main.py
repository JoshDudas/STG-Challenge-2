import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class AutomatedChromeBrowser (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')

    def test_checkForMake(self):
        self.driver.get("https://www.copart.com")
        self.driver.find_element(By.XPATH, "//input[@id='input-search']").send_keys("exotic")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.implicitly_wait(3)
        self.assertIn("PORSCHE", self.driver.find_element(By.XPATH,
                                                 "//table[@id='serverSideDataTable']//span[text()='PORSCHE']").text)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
