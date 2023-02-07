# 99 VIP 46、48，结合邮件发送测试报告
import HTMLTestRunner
import unittest
from time import sleep
from PO.page1.page import SearchPage
from selenium.webdriver.common.by import By
import zmail

class TestSearch(unittest.TestCase):
    def setUp(self):
        self.sp = SearchPage()

    def test_search01(self):
        self.sp.search_text("https://www.baidu.com",By.ID,"kw","邓超",By.ID,"su")
        self.sp.driver_sleep(1)

    def test_search02(self):
        self.sp.search_text("https://www.baidu.com",By.ID,"kw","邓超",By.ID,"su")
        self.sp.driver_sleep(1)

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(TestSearch('test_search02'))
    suite.addTest(TestSearch('test_search01'))
    f = open(r"./test_report46.html",'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="百度搜索页面的报告",description="这个报告主要记录百度首页的搜索功能")
    runner.run(suite)

    f.close() # 有些情况下没有这一步，会出现邮件没有内容的情况。因为文件打开写入数据，光标在最后一个位置，下面读取到的内容就是空白的，所以这里要关闭句柄
    with open('./test_report46.html','r',encoding='utf-8') as f:
        content_html = f.read()

    mail = {
        "subject":"测试报告总结",
        "content_html":content_html,
        "attachments":'./test_report46.html'
    }

    server = zmail.server("1192549787@qq.com","pwkqsbhbcamsggcd")
    server.send_mail("1192549787@qq.com",mail)





