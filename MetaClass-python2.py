''''#元类会将（ 你经常传给'type'的参数  ）作为自己的参数传入:Python2
 def upper_attr(future_class_name, future_class_parents, uppercase_attr):
    #返回一个对象，将属性都转为大写形式
    #选择不以"__"开头的属性
     attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))

     uppercase_attr = dict((name.upper(), value) for name , value in attrs)#将他们转为大写属性

     return type(future_class_name, future_class_parents, uppercase_attr)#通过type来类对象的创建

 __metaclass__ = upper_attr#这会应用到这个模块中的所有类

 class Foo(object):
    #也可以只在这定义__metaclass__，这样会作用到这个类中
    bar = 'bip'
'''
class UpperAttrMetaclass(type):
                                #'type'实际上是一个类，就像'str'和'int'一样
                                #'__new__'是在__init__之前被调用的特殊方法
                                #__new__是创建对象并返回的方法，而__init__只是将传入的参数初始化给对象
                                #很少用到'__new__'，除非想控制对象的创建
                                #这里创建的对象是类，希望能够自定义它，故改写'__new__'
    def __new__(cls, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if  not name.startwith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        #复用type.__new__方法
        #return type.__new__(cls, name, bases, uppercase_attr)
        return super(UpperAttrMetaclass, cls).__new__(cls, name, bases, uppercase_attr)
class MyFoo(object, metaclass = UpperAttrMetaclass):
    pass


#元类的主要用途是创建API，一个典型的例子是Django ORM。它允许这样定义：

class Person(models.Model):
    name = models.CharField(max_length = 30)
    age = models.InterField()

#如果这样定义：
guy = Person(name = 'bob', age = '35')
print(guy.age)
#这样并不会返回一个InterField对象，而是返回一个int,甚至可以直接从数据库中取出数据。
#Django框架将这些看起来复杂的东西通过暴露一个简单的使用元类的API将其简化，通过这个API重新创建代码，在背后完成真正的工作。
