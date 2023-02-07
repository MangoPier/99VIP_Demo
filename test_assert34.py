# 99 vip 34
# pytest的断言，不需要self.assert，直接用assert
import pytest



class TestAssert():
    # 传一个变量，判断变量是否为偶数，如果是偶数则用例通过
    def func1(self,a):
        if a%2 == 0:
            return True
        else:
            return False

    def test_func1(self):
        assert self.func1(2)

    def test_func2(self):
        assert self.func1(3)

    def test_in(self):
        list_demo = ["hello","world","hhh"]
        assert "h" in list_demo

    def test_notin(self):
        list_demo = [1,2,3,4]
        assert 5 not in list_demo

    def test_ass(self):
        # name = input("请输入用户名：")
        name = "99"
        # 断言可以在后面加上说明信息
        assert name=="99","变量的名字和最终预期的名字不一致，所以失败"

    # 异常信息断言
    def test_raiseexception(self):
        # 断言异常
        with pytest.raises(ZeroDivisionError) as exc:
            1/0
        #  判断异常的类型是否和预期一致
        assert exc.type==ZeroDivisionError

        # 断言异常的value值和预期是否一致
        assert "division by zero" in str(exc.value)




