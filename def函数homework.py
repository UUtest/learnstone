#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
def quadratic(a,b,c):
    if not (isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int, float))):
        raise TypeError('bad operand type')
    if b*b - 4*a < 0:
        return '方程式无解'
    elif a !=0 :
        x = (-b + math.sqrt(b*b - 4*a*c)) / (2*a)
        y = (-b - math.sqrt(b*b - 4*a*c)) / (2*a)
        return x,y
    elif b !=0:
        return -c / b
    elif c != 0:
        return 'c也需为0'
    else:
        return None
