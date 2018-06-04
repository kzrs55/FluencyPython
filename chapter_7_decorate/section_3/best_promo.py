# -*- coding: utf-8 -*-
__author__ = 'sun'

promos = []


def promotion(promo_func):
    promos.append(promo_func)
    return promo_func
