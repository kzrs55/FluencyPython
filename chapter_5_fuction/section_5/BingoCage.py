# -*- coding: utf-8 -*-
import random


class BingoCage:
    def __init__(self, items):
        self.items = list(items)
        random.shuffle(self.items)

    def pick(self):
        try:
            return self.items.pop()
        except IndexError:
            raise LookupError('pick from empty list')


    def __call__(self, *args, **kwargs):
        return self.pick()

if __name__ == '__main__':
    bingo = BingoCage(range(100))
    for i in range(10):
        print(i,bingo.pick())
    for i in range(10):
        print(i,bingo())

