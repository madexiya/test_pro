import pytest


# scope 默认function级别
# session 每个项目只执行一次，module是每个.py文件执行一次
# autouse 为测试用例自动应用方法
# 在方法参数传request，使用request.param接收params传入的参数
@pytest.fixture()
def login(request):
    print("登录方法")
    print(request.param)
    # yield 激活fixture的teardown方法
    yield ['username', 'password']
    print("teardown")
