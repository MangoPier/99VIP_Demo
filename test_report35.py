# 99 VIP 35

import pytest

class TestResult():
    def add(self,a,b):
        return a + b

    def test_add1(self):
        assert self.add(2,3) == 5

if __name__ == '__main__':
    pytest.main("-v")

# 命令行方法生成测试报告
# XML形式
# 当前目录
# pytest .\test_report35.py --junitxml=./log1.xml
# 指定目录
# pytest .\test_report35.py --junitxml=D:/log1.xml

# 通过pytest-HTML插件
# py.test .\test_report35.py --html=./test_report35.html
# pytest .\test_report35.py --html=./test_report35.html


