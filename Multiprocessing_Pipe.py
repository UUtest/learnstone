#Multiprocessing with Pipe

import multiprocessing as mul

def proc1(pipe):
    pipe.send('Hello')
    print('proc1 rec:', pipe.recv())

def proc2(pipe):
    print('proc2 rec:', pipe.recv())
    pipe.send('hello, too')

#Build a pipe
pipe = mul.Pipe()#这里的Pipe是双向的。

#Pipe对象建立的时候，返回一个含有两个元素的表，每个元素代表Pipe的一端(Connection对象)。
# 我们对Pipe的某一端调用send()方法来传送对象，在另一端使用recv()来接收。

#Pass an end of the pipe to process 1
p1 = mul.Process(target=proc1, args=(pipe[0],))
#Pass the another end of the pipe to process2
p2 = mul.Process(target=proc2, args=(pipe[1],))
p1.start()
p2.start()
p1.join()
p2.join()

