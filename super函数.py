class Fooa(object):
    def __init__(self):
        self.a = 'i \'m the a'
        print('a')

    def bar(self, message):
        print (message, 'from P')

class Foob(Fooa):
    def __init__(self):
        super(Foob, self).__init__()
        # super(Foob,self) 首先找到 Foob 的父类（就是类 Fooa）
        # 然后把类B的对象 Foob 转换为类 Fooa 的对象
        print ('b')

    def bar(self, message):
        super(Foob, self).bar(message)
        print('b bar function')
        print(self.a)

if __name__ == '__main__':
    foob = Foob()
    foob.bar('HELLo WORLD')
