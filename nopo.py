# 99 VIP 43
# 没有使用PO模式的情况
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class TestBaidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")

    def test_Case01(self):
        self.driver.find_element(By.ID,"kw").send_keys("陈小春")
        self.driver.find_element(By.ID,"su").click()

    def test_Case02(self):
        self.driver.find_element(By.ID,"kw").send_keys("李宇春")
        self.driver.find_element(By.ID,"su").click()

    def test_Case03(self):
        self.driver.find_element(By.ID,"kw").send_keys("周杰伦")
        self.driver.find_element(By.ID,"su").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
