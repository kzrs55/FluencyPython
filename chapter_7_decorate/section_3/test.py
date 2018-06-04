# -*- coding: utf-8 -*-
__author__ = 'sun'

b = 6


def test(a):
    a = 3
    global b  # 选择使用哪个变量作用域的变量
    print(a)
    print(b)
    b = 8


if __name__ == '__main__':
    test(3)
    from dis import dis
    dis(test)