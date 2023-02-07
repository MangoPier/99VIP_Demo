# 99 VIP P33
# 标记测试用例为预期失败
import pytest


class TestDemoXfail():
    def setup(self):
        print("测试用例的前置条件——开始执行")

    def teardown(self):
        print("测试用例的后置条件——执行结束")

    # 标记预期失败法一
    # 预期失败的装饰器，condition条件为真,run=False就不运行测试用例，结果直接标记Xfail
    @pytest.mark.xfail(condition=1<2,reason="因为此功能暂时未实现，预期应该是失败的",strict=False,run=False)
    # 预期失败的装饰器，condition条件为假
    # @pytest.mark.xfail(condition=1 > 2, reason="因为此功能暂时未实现，预期应该是失败的")
    def test_fail01(self):
        print("此功能暂时没有实现")
        assert 1 == 2

    # 标记预期失败法二，在测试用例内部调用函数
    def test_fail02(self):
        print("这个测试用例预期失败")
        pytest.xfail(reason="此功能暂时没有实现，以后的代码就不再执行")
        assert 2 == 3






