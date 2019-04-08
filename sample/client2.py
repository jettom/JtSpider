import socket

serverAddr = "192.168.1.4"
serverPort = 10000

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect((serverAddr, serverPort))

while True:
    clientInput= input(' please input > ')
    client_sock.send(clientInput.encode())
    response = client_sock.recv(1024)
    print (response)

client_sock.close()