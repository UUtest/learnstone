# -*- coding: utf-8 -*-
L = [('Bob',75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
     return str(t[0])
#L2 = sorted(L, key = by_name,reverse =True)
L2 = sorted(L, key = by_name)
print(L2)
