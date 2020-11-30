# 传入fixture装饰的方法，在用例执行前先执行传入的方法
def test_case1(login):
    print(f"case1 login = {login}")


def test_case2():
    print("case2")


def test_case3():
    print("case3")
