
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

#转换函数，先把实例通过student2dict()函数转换成dict
def student2dict(self):
    return {
        'name':self.name,
        'age':self.age,
        'score':self.score
    }
#可选参数default把任意一个对象变成一个可序列化成JSON的对象
s = Student('Bob', 20, 88)
#然后再序列化为JSON
print(json.dumps(s, default=student2dict))

#任意class的实例变成dict，class的实例都有__dict__属性
print(json.dumps(s, default=lambda obj: obj.__dict__))
#把JSON反序列化为一个对象实例

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
#用loads()方法首先转换出一个dict对象，传入object_hook函数把dict转换为实例
print(json.loads(json_str, object_hook = dict2student))