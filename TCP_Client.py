#导入socket库
import socket
# #创建一个socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# #建立连接
# s.connect(('www.sina.cn',80))
# #发送请求内容
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# #接受数据
# buffer = []
# while True:
#     #最多接受1K数据
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
#
# data = b''.join(buffer)
# #关闭连接
# s.close()
# #网页内容保存到文件：
# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
# #把接收的数据写入文件：
# with open('sina.html','wb') as e:
#     e.write(html)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#建立连接
s.connect(('127.0.0.1',9999))
#接受欢迎消息：
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    #发送数据
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()