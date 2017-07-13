import unittest#需引入Python自带的unitest模块
from mydict import Dict
class TestDict(unittest.TestCase):#编写测试类，从unitest.TestCase继承

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_init(self):      #以test开头的方法就是测试方法，不以test开头的非test方法，测试时不会被执行
        d = Dict(a = 1, b = 'test')
        self.assertEqual(d.a, 1)#unittest.TestCase提供了很多内置的条件判断，只需调用这些方法就可以断言输出
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):#对每一类测试都需编写一个test_xxx()方法。
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')#最常用的断言assertEqual()，断言两个值相等

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)#断言d中是否有key的key
        self.assertEqual(d['key'], 'value')#断言d的'key'属性的值和value相等

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):#另一种断言，期待抛出指定类型的Error
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):#执行value=d.empty，若抛出Attribute，则断言
            value = d.empty

if __name__ == '__main__':#这样就可以把mydict_test.py当成正常的脚本运行：python mydict_test.py
    unittest.main()#另一种方法是在命令行通过参数-m unittest直接运行单元测试

