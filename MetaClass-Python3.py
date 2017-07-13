#metaclass 是类的模版，所以必须从'type'类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)
#在定义类的适合还要只是使用ListMetaclass来定制类，传入关键字参数metaclass：
class MyList(list, metaclass = ListMetaclass):
    pass
#当传入关键字参数metaclass时，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，在此，可以修改类的定义

'''
__new__()方法接收到的参数依次是：

1.当前准备创建的类的对象；

2.类的名字

3.类继承的父类的集合

4.类的方法集合
'''