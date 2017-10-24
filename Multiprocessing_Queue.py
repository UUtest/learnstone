from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码：
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)#放入队列
        time.sleep(random.random()) #random.random()返回随机生成的实数，范围：0-1;
                                 # time.sleep()推迟调用线程的执行

# 读数据进程执行的代码：
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)#get()方法获取 返回指定键的值
        print('Get %s from queue' % value)

if __name__ == '__main__':
    #父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))#往Queue里写数据;传入执行函数和 函数的参数，创建出一个实例
    pr = Process(target=read, args=(q,))#从Queue中读数据

    #启动子进程pw，写入：
    pw.start()#Process to write: 70124
              # Put A to queue...

    #启动子进程pr，读取：
    pr.start()#Process to read: 70125
              # Get A from queue

    #等待pw结束：
    pw.join()#join方法可以等待子进程结束后再继续往下运行，，常用于进程间的同步
             #write()进行循环，然后value='B'，把'B'放入了队列中，即写入了Queue中，产生结果：
             #Put B to queue...
             #Get B from queue

    #pr进程里是死循环，无法等待其结束，只能强行终止：
    pr.terminate()#'A'，'B', 'C'循环结束后，强行终止了