from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()         #time.time()获取当前时间戳浮点数
    time.sleep(random.random() * 3) #random.random()返回随机生成的实数，范围：0-1
    end = time.time()
    print('Task %s runs %0.2f seconds' % (name, (end - start)))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)                                 #task0，1，2，3是立刻执行的，而task4是等待前面某个task完成后才执行
    for i in range(4):
        p.apply_async(long_time_task, args = (i,)) #pool.apply_async是异步方式调用：连续提交任务
                                                #pool.apply是同步方式调用：下一个task需要等待上一个task完成后才能开始运行
    print('Waitting for all subprocesses done...')
    p.close()                               #调用join()之前必须close，调用close()之后不能添加新的process
    p.join()                                #在对pool调用join()会等待所有子进程执行完毕
                                            #join()一般用于进程间的同步，join()可以等待子进程结束后继续运行
    print('All subprocesses done.')
'''
Parent process 18159.
Waitting for all subprocesses done...
Run task 0 (18160)...
Run task 2 (18162)...
Run task 1 (18161)...
Run task 3 (18163)...
Task 2 runs 0.13 seconds
Run task 4 (18162)...
Task 1 runs 0.25 seconds
Task 3 runs 1.65 seconds
Task 0 runs 2.04 seconds
Task 4 runs 2.10 seconds
All subprocesses done.
'''