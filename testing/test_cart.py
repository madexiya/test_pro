import pytest


def test_cart1():
    print('购物车用例1')


def test_cart2():
    print('购物车用例2')


# 参数化结合fixture使用
# 1、传入值和数据
# 2、传入一个fixture方法，将数据传入到fixtrue方法中，fixtrue方法使用request来接收这组数据
#    在方法体里使用request.param 来使用这个数据
@pytest.mark.parametrize('login', [
    ('username', 'password'),
    ('username1', 'password1')
], indirect=True)
def test_cart3(login):
    print('购物车用例3')


@pytest.mark.parametrize('a', [1, 2, 3])
@pytest.mark.parametrize('b', [4, 5, 6])
def test_data(a, b):
    print(a, b)
