# -*- coding:utf-8 -*-
import socket

host = "192.168.1.4" #お使いのサーバーのホスト名を入れます
port = 8080 #クライアントと同じPORTをしてあげます

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversock.bind((host,port)) #IPとPORTを指定してバインドします
serversock.listen(10) #接続の待ち受けをします（キューの最大数を指定）

print ('Waiting for connections...')
clientsock, client_address = serversock.accept() #接続されればデータを格納

while True:
    rcvmsg = clientsock.recv(1024)
    print ('Received -> %s' % (rcvmsg.decode()))
    if rcvmsg == '':
      break
    print ('Type message...')
    s_msg = input()
    if s_msg == '':
      break
    print ('Wait...')

    clientsock.sendall(s_msg) #メッセージを返します
clientsock.close()