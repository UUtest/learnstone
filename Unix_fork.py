#Only works on Unix/Luinx/Mac

import os
print('Process (%s) start...' % os.getpid())

pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
          #返回0时，当前为子进程，getpid子进程id，getppid父进程id
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))  #fork返回不为0时，是父进程返回的子进程id，
                                                                            # 当前为父进程，pid返回子进程的id，os.getpid()返回当前进程即父进程id
