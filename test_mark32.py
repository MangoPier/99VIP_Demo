import pytest


class TestMark():
    @pytest.mark.mark1
    def test_m1(self):
        list_demo = [1,2,3,4]
        assert 1 in list_demo

    @pytest.mark.smoke
    def test_m2(self):
        list_demo = [1,2,3,4]
        assert 3 in list_demo

    # 允许添加多个标签，那么可以通过mark1，也可以通过smoke执行到这个测试用例
    @pytest.mark.mark1
    @pytest.mark.smoke
    def test_m3(self):
        list_demo = [1,2,3,4]
        assert 5 in list_demo

# 如果给类添加了标签，那么这个类当中的所有测试用例test_开头的方法都会被执行
@pytest.mark.mark2
class TestMark2():
    def test_m4(self):
        msg = "hhhhh i o u"
        assert "m" not in msg


if __name__ == '__main__':
    pytest.main()

# 可以在命令行执行
# 可以结合与或非
# pytest -m "smoke or mark2" -v
# pytest -m "smoke and mark1" -v
# pytest -m "not mark1" -v