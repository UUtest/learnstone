import asyncio

#@asyncio.coroutine把一个generator标记成coroutine类型，然后把这个coroutine扔到EventLoop中执行
@asyncio.coroutine
def hello():
    print('Hello world')
    #异步调用asyncio.sleep(1):
    #yield from可以让我们方便调用另一个generator
    #asyncio.sleep()也是一个coroutine,所以它并不会被线程等待，直接中断并执行下个消息循环
    #asyncio.sleep()返回时，线程可以从yield from 拿到返回值(None)，并执行下一个语句
    r = yield from asyncio.sleep(1)
    print("Hello again!")

#获取EventLoop：
loop = asyncio.get_event_loop()
#执行
loop.run_until_complete(hello())
loop.close()