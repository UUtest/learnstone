import socket
import threading
import time
#创建一个基于IPv4和TCP协议的Socket：
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#端口号需要预先指定,监听端口
s.bind(('127.0.0.1',9999))
#开始监听接口，传入的参数是指定的最大连接数
s.listen(5)
print('Wating for connection...')
#服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接:

def tcplink(sock, addr):
    print('Accept new connection from %s %s...' % addr)
    sock.send(b'Welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s: %s closed' % addr)
while True:
    #接受一个新连接
    sock, addr = s.accept()
    #创建新线程来处理TCP连接：
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
#每个新连接必须创建新线程（或进程）