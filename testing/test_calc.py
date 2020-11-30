import pytest

from pythoncode.calc import Calculator


# 模块级别 setup和teardown，在整个模块（文件）前后分别执行
def setup_module():
    print("模块级别 setup")


def teardown_module():
    print("模块级别 teardown")


# 函数级别 setup和teardown
def setup_function():
    print("函数级别 setup")


def teardown_function():
    print("函数级别 teardown")


class TestCalc:
    # 类级别 setup和teardown
    def setup_class(self):
        self.cal = Calculator()
        print("类级别 setup")

    def teardown_class(self):
        print("类级别 teardown")

    # 类里面的setup和teardown，运行在方法调用的前和后
    # 每条类里面的测试用例前后分别执行 setup和teardown
    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")

    @pytest.mark.add
    @pytest.mark.parametrize('a,b,result', [
        (1, 1, 2),
        (2, 2, 4),
        (100, 100, 200),
        (0.1, 0.1, 0.2),
        (-1, -1, -2)
    ], ids=["int", "int1", "bignun", "float", "fushu"])
    def test_add(self, a, b, result):
        # cal = Calculator()
        assert result == self.cal.add(a, b)

    @pytest.mark.add
    def test_add1(self):
        # cal = Calculator()
        assert 3 == self.cal.add(1, 2)

    @pytest.mark.div
    def test_div(self):
        # cal = Calculator()
        assert 1 == self.cal.div(1, 1)
