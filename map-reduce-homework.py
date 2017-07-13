#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce
'''def str2float(s):
    n = 10 ** -(s[::-1].index('.'))
    return n*reduce(lambda x, y: x * 10 + y, [int(a) for a in s if a is not '.'])

def str2float(x):
    list(x)
    position = x.index('.')
    integer1 = list(map(int, x[:position]))
    integer2 = reduce(lambda x, y: x * 10 + y, integer1)
    decimal1 = list(map(int, x[:position:-1]))
    decimal2 = reduce(lambda x, y: x * 0.1 + y, decimal1)
    return integer2 + 0.1 * decimal2
'''

def str2float(s):
    import functools
    temp_s = s if '.' in s else s+'.'
    d, f = temp_s.split('.')
    return functools.reduce(lambda x,y: x*10 + y, map(int, d), 0) + \
           functools.reduce(lambda x,y: x/10 + y, map(int, reversed('0'+f)), 0)

'''
CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2float(s):
    nums = map(lambda ch:CHAR_TO_FLOAT[ch],s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)
'''                
            
        
print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))
print(str2float('.'))
