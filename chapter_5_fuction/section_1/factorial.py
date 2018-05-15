# -*- coding: utf-8 -*-
def fabonacci(n):
    """
    f（n）= f（1）+f(2)+...f(n-1);
    :param n:
    :return f(n)
    """
    return 1 if n == 1 or n == 2 else fabonacci(n - 1) + fabonacci(n - 2)


if __name__ == '__main__':
    # print(factorial(10))
    print(fabonacci.__doc__)
    # print(type(factorial))
