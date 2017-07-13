class Dict(dict):#创造一个有dict功能的类，并可以把key作为属性，输出value值(使用__getattr__()函数)
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):#访问对象的item属性时，若无对应属性或方法，则调用这个方法处理
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):#setattr函数赋给对象self的key属性一个属性值value
        self[key] = value
