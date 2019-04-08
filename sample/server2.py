import socket

class EchoServer:
    def __init__(self, addr, port):
        self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_sock.bind((addr, port))
        self.server_sock.listen(1)

    def start(self):
        conn, addr = self.server_sock.accept()

        while True:
           print ("connected by", addr)
           data = conn.recv(1024)
           if not data: break
           conn.send(data)

        conn.close()

server = EchoServer("192.168.1.4", 10000)
server.start()