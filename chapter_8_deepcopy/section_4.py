# -*- coding: utf-8 -*-
__author__ = 'sun'

class HauntedBus:

    def __init__(self,passengers = []):
        self.passengers = passengers

    def pick(self,name):
        self.passengers.append(name)

    def drop(self,name):
        self.passengers.remove(name)

if __name__ == '__main__':

