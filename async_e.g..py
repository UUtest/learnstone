import asyncio
import time
now = lambda : time.time()
async def do_some_work(x):
    print('Watting:', x)

start = now()

coroutine = do_some_work(2)

loop = asyncio.get_event_loop()
#创建task：
#asyncio.ensure_future(coroutine) 和 loop.create_task(coroutine)都可以创建一个task
#task = asyncio.ensure_future(coroutine)
task = loop.create_task(coroutine)
#当传入一个协程，其内部会自动封装成task,task是Future的子类：isinstance(task, async.Future)=Ture
print(task)#创建task后，task在加入事件循环之前是pending状态

#run_until_complete的参数是一个futrue对象
loop.run_until_complete(task)
print(task)#打印的是task的finished状态

print('TIME: ', now() - start)
