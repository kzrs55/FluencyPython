# -*- coding: utf-8 -*-
__author__ = 'sun'


def avg():
    list = []

    def averager(value):
        list.append(value)
        return sum(list) / len(list)

    return averager


if __name__ == '__main__':
    print(avg()(10))
    print(avg()(11))
    print(avg()(12))
