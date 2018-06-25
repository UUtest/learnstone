def consumer():
    r = ''
    while True:
        #2.consumer通过yield拿到传递的None，yield跳出
        #5.从上次跳出的地方，将生成器上一次挂起的yield语句的值指定为n
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'
        # 6.consumer到这里开始循环，通过上一步的yield把结果传回

def produce(c):
    #1.启动生成器
    c.send(None)
    #3.接着往下执行，产生数据
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...'%n)
        #4.产生的数据n=1，通过send切换到consumer执行
        r = c.send(n)
        #7.跳出之后，produce拿到consumer处理的结果'200 OK'
        print('[PRODUCER] Consumer return: %s' % r)
        #8.继续生产下一条消息
    #9.produce生产结束，通过close()关闭consumer
    c.close()

#创建一个generator对象
c = consumer()
produce(c)
