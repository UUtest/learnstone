class Chain(object):
    def __init__(self, path = 'GET '):
        self._path = path

    def __getattr__(self, path1):
        return Chain('%s/%s' % (self._path, path1)) #.user调用__getattr__得到/user

    def __call__(self, path2):
        return Chain('%s/%s' % (self._path, path2)) #通过__call__()方法
                                                    #('Mojian')调用了实例自身，得到了/Mojian 

    def __str__(self):
        return self._path

    __repr__ = __str__
    
print(Chain().status.user('Mojian').repos)
