# -*- coding: utf-8 -*-
import functools

from chapter_7_decorate.section_7.clock import clock

__author__ = 'sun'

@functools.lru_cache()
@clock
def fibonacci(n):
    return n if n<2 else fibonacci(n-1)+fibonacci(n-2)

if __name__ == '__main__':
    print(fibonacci(6))