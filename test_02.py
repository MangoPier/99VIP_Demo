import pytest

# 除了对单个测试用例跳过，还可以对整个类的测试用例跳过，也可以针对模块
@pytest.mark.skip
class TestDemo02():
    # 定义全局变量
    name = "199"
    pwd = "123456"
    mark = pytest.mark.skip(reason="无条件跳过")

    # 有条件地跳过：表达式为真，就跳过测试用例。
    # 如果用户名不是99，测试用例不执行
    @pytest.mark.skipif(condition=name!="99",reason="用户错误，没有必要判断密码")
    def test_pwd00(self):
        assert self.pwd == "123456"

    # 批量跳过测试用例，那么可以在前面先定义一个全局变量mark，之后在每个需要跳过的测试用例前面加一个@mark
    @mark
    def add(self,a,b):
        self.c = a + b
        return self.c

    @mark
    def test_add1(self):
        assert self.add(1,1) == 2

    # 无条件跳过测试用例
    @pytest.mark.skip(reason="就是没有理由")
    def test_add2(self):
        assert self.add(2,2) == 4

    # @pytest.mark.skipif(condition="")
    def test_add3(self):
        assert self.add(2,2) == 4


if __name__ == '__main__':
    pytest.main(["test_02.py"])



