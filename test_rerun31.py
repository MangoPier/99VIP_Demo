# 99 VIP P31
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest



class TestBaiDu():
    # pytest框架里面前置后置都是小写的
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")

    def teardown(self):
        self.driver.quit()

    # 重跑机制
    @pytest.mark.flaky(reruns=2,run_delay=1)
    def test_baidu(self):
        self.driver.find_element(By.ID,"kw").send_keys("汇顶科技")
        self.driver.find_element(By.ID,"ku").click()


# if __name__ == '__main__':
#     pytest.main(["test_rerun21.py"])





