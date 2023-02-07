# 99 VIP 36
# 测试夹具
import pytest

# 定义一个测试类
class TestFixture():
    # setup是全局的
    def setup(self):
        print("----测试用例开始执行")

    # 定义一个测试夹具
    @pytest.fixture()
    def func_data(self):
        data = 99
        return data

    # 定义测试用例
    # 测试夹具定义的函数名可以用作测试用例的参数名（变量名）
    def test_data(self,func_data):
        # 判断前置条件的这个数据是不是我们需要的99
        assert func_data == 99

    # 定义一个测试夹具，准备一个列表数据
    @pytest.fixture()
    def list_data(self):
        list_data = [11,22,33]
        return list_data

    def test_list(self,list_data):
        assert 33 in list_data


if __name__ == '__main__':
    pytest.main("-v")

