import pytest

if __name__ == '__main__':
    # 法一
    # pytest.main(["test_demo30.py"])
    # 法二,nodeid方法。如果执行的py文件跟main文件不是同一个目录，那么需要在py文件前加一个路径
    # pytest.main(["test_demo30.py::TestDemo::test_add"])
    # 法二没有把print(c)打印出来
    # 法三，-s显示print的信息到控制台
    # pytest.main(["-s"])
    # 法四：-k，执行关键字表达式匹配筛选的测试用例
    # pytest.main(["-k","test_Demo02"])
    # pytest.main(["-k=test_add"])
    # pytest.main(["-k=TestDemo and not 03"])
    # 法5：-x遇到失败的测试用例就停止
    # pytest.main(["-x"])
    # 法6，--maxfail=num，最多允许多少条执行失败，达到了后面的测试用例就不再执行
    # pytest.main(["--maxfail=2","test_01.py"])
    # 法7：-v显示详细执行信息
    # pytest.main(["-v"])
    # 法8：-m，运行指定标签的测试用例
    pytest.main(["-m","mark2"])