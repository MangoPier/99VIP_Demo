# 99 VIP 36
import pytest


@pytest.fixture()
def func_00():
    print("这是一个前置条件")
    return 1,2,3

@pytest.mark.usefixtures("func_00")
class TestFixtures():
    @pytest.fixture()
    def func_01(self):
        print("这是前置条件1")

    @pytest.fixture()
    def func_02(self):
        print("这是前置条件2")

    @pytest.fixture()
    def func_03(self):
        print("这是前置条件3")

    @pytest.mark.usefixtures("func_01","func_02")
    def test_demo01(self):
        print("这是测试用例1")

    @pytest.mark.usefixtures("func_03")
    def test_demo02(self):
        print("这是测试用例2")

    def test_demo03(self,func_00):
        assert 12 in func_00

if __name__ == '__main__':
    pytest.main("-v")


