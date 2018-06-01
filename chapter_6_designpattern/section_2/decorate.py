# -*- coding: utf-8 -*-
__author__ = 'sun'
def deco(func):
    def inner():
        print("hello world")
    return inner

@deco
def test():
    print("John Smith")

if __name__ == '__main__':
    test()
    print(test)