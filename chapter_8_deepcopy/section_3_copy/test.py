# -*- coding: utf-8 -*-
__author__ = 'sun'

#浅拷贝拷贝列表对象的时候，任意改变某个可变的列表对象将会影响原先的被拷贝对象
if __name__ == '__main__':
    l1 = [3,[66,55,44],(7,8,9)]
    l2 = list(l1)
    l1.append(100)
    l1[1].remove(55)
    print('l1',l1)
    print('l2',l2)
    l2[1]+=[33,22]
    l2[2]+=(10,11)
    print('l1',l1)
    print('l2',l2)
