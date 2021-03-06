# -*- coding: utf-8 -*-
def fact(n):
    '''

    >>> fact(3)
    6
    >>> fact(1)
    1
    >>> fact(0)
    Traceback(most recent call last):
        …                                #”…"表示中间烦人的输出
    ValueError
    '''
    if n < 1:
        raise ValueError
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()