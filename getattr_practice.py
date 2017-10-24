'''class Student(object):
    def __init__(self):
        self.name = 'Mojian'
    def __getattr__(self, attr):
        if attr == 'age':
            return lambda:25
        raise AttributeError('\'Student\' object has no attribute \'%s \' ' % attr)
s = Student()
#print(s.age)
    
print(s.score)
'''
class Chain(object):
    def __init__(self, path = 'Get '):#定义第一个实例
        self._path = path

    def __getattr__(self, path):    #调用.user('Mojian')时,转到__getattr__调用，path指向user
        return Chain('%s/%s' % (self._path, path))  #在传给Chain中把self和path连起来，返回Get/user

    #调用Chain———>__init__，因Chain()将生成一个实例，这个实例后跟着('Mojian'),将调用__call__

    def __call__(self, path):   #使user('Mojian')调用自身实例，path指向Mojian
        return Chain('%s/%s' % (self, path))#传给Chain的过程中，又把原来的 'Get/user'和Mojian连起来了

    #继续走Chain()，把Get /user/Mojian给了_path，后面跟着的imp.repos继续调用__getattr__

    def __str__(self):
        return self._path   #返回_path中生成的字符串

    __repr__ = __str__

print(Chain().users('Mojian').imp.repos('two'))#外面是一个print，里面是Chain()的实例，所以会调用str，返回_path