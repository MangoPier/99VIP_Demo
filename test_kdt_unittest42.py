# 99 VIP 42
# 关键字驱动，结合unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest


class Login():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_url(self,url):
        self.driver.get(url)

    # 记得这里是返回元素，否则input_text无法使用send_keys属性
    def get_element(self,name,value):
        return self.driver.find_element(name,value)

    def input_text(self,name,value,keys):
        self.get_element(name,value).send_keys(keys)

    def click(self,name,value):
        self.get_element(name,value).click()

    def driver_quit(self):
        self.driver.quit()

    def driver_sleep(self,time):
        sleep(time)

    # 定义一个方法，完整地实现登录功能
    def login(self,url,name,value,key,name2,value2,key2,name3,value3,time):
        self.open_url(url)
        self.input_text(name,value,key)
        self.input_text(name2,value2,key2)
        self.click(name3,value3)
        self.driver_sleep(time)
        # self.driver_quit()

# 定义一个测试类
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.login = Login()

    def test_open(self):
        self.login.open_url("http://39.101.167.251/qftest/user/login.html")

    def test_login(self):
        self.login.login("http://39.101.167.251/qftest/user/login.html",By.ID,"username","test2021001",By.ID,"password","123456",By.XPATH,'/html/body/div[2]/div/form/div/a',3)

    def test_login2(self):
        self.login.login("http://39.101.167.251/qftest/user/login.html",By.ID,"username","test2021001",By.ID,"password","1234567",By.XPATH,'/html/body/div[2]/div/form/div/a',3)

    @classmethod
    def tearDownClass(cls):
        print("这个类的后置条件")
        cls.login = Login()
        cls.login.driver_quit()


if __name__ == '__main__':
    # 没有使用unittest框架可以以下操作运行：
    '''
    login = Login()
    # 法一
    """
    login.open_url("http://39.101.167.251/qftest/user/login.html")
    login.input_text(By.ID,"username","test2021001")
    login.input_text(By.ID,"password","123456")
    login.click(By.XPATH,'/html/body/div[2]/div/form/div/a')
    login.driver_sleep(3)
    login.driver_quit()
    """
    # 法二: 用到33行封装的方法
    login.login("http://39.101.167.251/qftest/user/login.html",By.ID,"username","test2021001",By.ID,"password","123456",By.XPATH,'/html/body/div[2]/div/form/div/a',3)
    login.driver_quit()
    '''
    suite = unittest.TestSuite()
    suite.addTest(TestLogin("test_open"))
    suite.addTest(TestLogin("test_login"))
    suite.addTest(TestLogin("test_login2"))
    runner = unittest.TextTestRunner()
    runner.run(suite)