#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'Simple ORM using metaclass'

#Object Relational Mapping ，对象-关系 映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，所有类只能动态定义

'''第一，按编写的下面的接口实现该ORM'''
#首先定义Field类，它负责保存数据库表的字段名和字段类型
class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type =column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

#在Field的基础上，进一步定义各种类型的Field：
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


#第三步，编写ModelMetaclass：
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings     #保存属性和列的映射关系
        attrs['__table__'] = name           #假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)
#第四部，基类Model：
class Model(dict, metaclass = ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' Object has no attribute '% s' " % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

'''第二，编写调用接口（定义一个User类来操作对应的数据库表User）：'''
# 父类Model和属性类型IntgerField、StringField都是ORM框架提供的
class User(Model):
    #定义类的属性到列（数据库的列）的映射
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

#创建一个实例：
u = User(id = 12345, name = 'Mojian', email = 'test&orm.org', password = 'my-pwd')

#保存到数据库：
u.save()