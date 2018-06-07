# -*- coding: utf-8 -*-
__author__ = 'sun'

registry = []
def register(func):
    print('running register(%s)'% func)
    registry.append(func)
    return func

@register
def f1():
    print('running main()')

if __name__ == '__main__':
    f1()
