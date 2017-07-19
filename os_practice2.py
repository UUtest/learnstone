#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

'''
def search_file(dir, name):
    for x in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, x)):
            if name in os.path.split('x')[0]:
                print('%s, %s' % (dir, x))
        if os.path.isdir(os.path.join(dir, x)):
            search_file(os.path.join(dir, x), name)

print(search_file('/Users/lizhengdao/PycharmProjects/learnPython3/', 'w'))
''''''
rootDir = os.path.abspath('.')
def getPath(name):
    for lists in os.listdir(rootDir):
        path = os.path.join(rootDir, lists)
        if lists == name:
            return path
        elif os.path.isdir(path):
            getPath(path)
print(getPath('s'))
'''

def serch_file(pwd, name):

    for x in os.listdir(pwd):                       #列出pwd路径下所有的目录
        abspathpwd = os.path.join(pwd, x)
        if os.path.isfile(abspathpwd):      #如果abspathpwd路径是一个存在的文件
            if name in os.path.splitext(x)[0]:                   #如果文件名包括name，打印出绝对路径
                print(abspathpwd)
        if os.path.isdir(abspathpwd):       #如果abspathpwd路径是一个存在的目录,则继续进行循环
            serch_file(abspathpwd, name)

pwd = os.path.abspath('.')  #定义pwd为当前目录绝对路径
name = input('serch file: ')#要求输入要serch的文件名
serch_file(pwd, name)#进行调用
