import functools
def log(text = ''):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('begin call %s %s():' % (text, func.__name__))
            func(*args, **kw)
            print('end call %s %s():' % (text, func.__name__))
        return wrapper
    return decorator
