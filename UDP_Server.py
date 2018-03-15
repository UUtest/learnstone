import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#绑定端口
s.bind(('127.0.0.1',9999))
#创建socket，SOCK_DGRM指定了这个Socket类型是UDP，不许调用listen()方法，直接收取客户端的数据
print('Bind UDP on 9999...')
while True:
    #接受数据
    data, addr = s.recvfrom(1024)#recvfrom()方法返回数据和客户端的地址与端口，
                                # 这样服务器收到数据后，直接调用sendto()就可以把数据用UDP发给客户端
    print('Recevied from %s: %s' % addr)
    s.sendto(b'Hello, %s!' % data, addr)
    