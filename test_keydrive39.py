# 99 VIP P39
# 关键字驱动
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# 案例：通过关键字驱动实现百度搜索功能

# 先不加关键字驱动来实现百度搜索
"""
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.find_element(By.ID,"kw").send_keys("陈小春")
driver.find_element(By.ID,"su").click()

sleep(3)
driver.quit()
"""
# 优化代码
# 将打开的页面、元素定位方式、搜索内容都设置为关键字驱动，提高代码的复用率
class SearchKeys():
    def get_driver(self):
        driver = webdriver.Chrome()
        return driver

    def __init__(self):
        self.driver = self.get_driver()

    # 定义一个方法，来打开需要测试的页面
    def open_url(self,url):
        self.driver.get(url)

    def locator(self,name,value):
        return self.driver.find_element(name,value)

    def input_text(self,name,value,keys):
        self.locator(name,value).send_keys(keys)

    def click(self,name,value):
        self.locator(name,value).click()

    def driver_quit(self):
        self.driver.quit()

    def driver_sleep(self,time):
        sleep(time)

if __name__ == '__main__':
    searchkeys = SearchKeys()
    searchkeys.open_url("https://www.baidu.com")
    searchkeys.input_text(By.ID,"kw","陈小春")
    searchkeys.click(By.ID,"su")
    searchkeys.driver_sleep(3)
    searchkeys.driver_quit()
