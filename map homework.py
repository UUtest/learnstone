# -*- coding: utf-8 -*-
def normallize(name):
    return name.capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normallize, L1))
print(L2)
