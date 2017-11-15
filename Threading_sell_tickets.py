#模拟多线程售票
import threading
import time
import os

def doChore():
    time.sleep(0.5)#方便以后改进程序，添加其他操作

def booth(tid):
    global i
    global lock#声明i，lock为全局变量，从而让多线程共享i和lock
               #如果不声明，因i、lock是不可变对象，将会被当成一个局部变量；可变则不需声明。
    while True:
        lock.acquire()#只有一个线程可以Lock(获取lock)，继续执行代码，其他线程等待直到获取锁
        if i != 0:
            i = i - 1#售票，i储存剩余票数
            print(tid,':now left:', i)#剩票数
            doChore()#依然在Lock内部，故可以进行其他使用共享资源，如：打印剩票
                     #time.sleep(0.5)等待了0.5s，代表额外的操作可能花费的时间
        else:
            print('Thread_id', tid, 'no more tickets')
            os._exit(0)#直接退出售票过程
                       #sys.exit(n) 退出程序引发SystemExit异常, 可以捕获异常执行些清理工作. n默认值为0, 表示正常退出.
                       #os._exit(n), 直接退出, 不抛异常, 不执行相关清理工作. 常用在子进程的退出.
                       #exit()/quit(), 跑出SystemExit异常. 一般在交互式shell中退出时使用.
        lock.release()#除去障碍
        doChore()#Lock此时已被释放，无法再使用共享资源，可以做一些不使用共享资源的事情（喝水，找零）

#启动主要功能：
i = 100#总票数
lock = threading.Lock()#创建一个锁，即互斥锁；为了防止其他线程同时获取票数；同步线程对i的修改

#开始10个线程
for k in range(10):
    new_thread = threading.Thread(target=booth,args=(k,))#设置线程；threading.Thread代表线程
                                                         #target:传入（函数）来运行
                                                         #args: 传入要调用的参数
    new_thread.start()
