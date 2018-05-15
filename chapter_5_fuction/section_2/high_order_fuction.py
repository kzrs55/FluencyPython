# -*- coding: utf-8 -*-

def factorial(n):
    """
    阶乘函数
    :param n:
    :return n!:
    """
    return 1 if n == 0 or n == 1 else factorial(n - 1) * n


if __name__ == '__main__':
    list1 = [11, 22, 33, 44, 55, 66, 77, 88, 99, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(sorted(list1))  # 按照大小进行排序
    list2 = ['abc', 'ab', 'abcd', 'abcde', 'abcdef']
    print(sorted(list2, key=len))  # 按照字符串长度进行排序
    # 反向排序
    for i in reversed(list2):
        print(i)

    # 构建0！到5！的阶乘列表
    print([factorial(n) for n in range(6)])

    #
    
