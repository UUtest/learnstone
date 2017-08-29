#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from multiprocessing import Process
import os

def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))#传入执行函数和 函数的参数，创建出一个实例
    print('Child process will start.')
    p.start()                                   #用start方法启动
    p.join()                                    #join方法可以等待子进程结束后再继续往下运行，，常用于进程间的同步
    print('Child process end.')