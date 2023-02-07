# 99 VIP 37

# 数据驱动
# ddt

import unittest
from selenium import webdriver
from ddt import ddt, data, file_data, unpack
from selenium.webdriver.common.by import By
from time import sleep

# 在类的外面记得加上@ddt
@ddt
class TestBaidu(unittest.TestCase):
    # 定义前置条件
    @classmethod
    def setUpClass(cls):
        print("这是类的前置条件")
        cls.driver = webdriver.Chrome()
        cls.url = "https://www.baidu.com"

    # 定义一个方法，实现百度的搜索功能
    def baidu_search(self, keys):
        self.driver.get(self.url)
        self.driver.find_element(By.ID, "kw").send_keys(keys)
        self.driver.find_element(By.ID, "su").click()

    # ddt结合列表：测试用例上面需要放装饰器@data@unpack
    # @data(["陈小春"], ["张学友"])
    # @data(["1","陈小春"],["2","张学友"])
    # ddt结合字典
    @data({"case":1,"keys":"陈小春"},{"case":2,"keys":"周杰伦"})
    @unpack # 这是解包
    def test_search(self, case,keys):
        print(case)
        self.baidu_search(keys)
        sleep(2)
        self.assertEqual(self.driver.title, keys + "_百度搜索")


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
