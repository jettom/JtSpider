#coding:utf-8
#TCP客户端的创建和运行

#coding:utf-8
import socket
#初始化Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#连接目标的ip和端口
s.connect(('127.0.0.1', 9999))
# 接收消息
print('-->>'+s.recv(1024).decode('utf-8'))
# 发送消息
s.send(b'Hello,I am a client')
print('-->>'+s.recv(1024).decode('utf-8'))
s.send(b'exit')
#关闭套接字
s.close()

'''
-->>Hello,I am server!
-->>Loop_Msg: Hello,I am a client!

Process finished with exit code 0
'''
