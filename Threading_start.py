import time, threading

#新线程执行的代码
def loop():
    print('thread %s is running...' % threading.current_thread().name)#threading.current_thread().name，它永远返回当前线程的实例名字。
    n = 0
    while n < 5:
        n  = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(0.5)
    print('thread %s ended' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)#主线程
t = threading.Thread(target=loop, name='LoopThread')#创建子线程实例
t.start()#启动子线程
t.join()
print('thread %s ended' % threading.current_thread().name)#输出：主线程关闭
'''
thread MainThread is running...#主线程名称：MainThread
thread LoopThread is running...#创建子线程
thread LoopThread >>> 1
thread LoopThread >>> 2
thread LoopThread >>> 3
thread LoopThread >>> 4
thread LoopThread >>> 5
thread LoopThread ended
thread MainThread ended
'''