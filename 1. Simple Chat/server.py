#!/usr/bin/env python
import socket

IP = "localhost"
PORT = 8081

class Servidor():
    def __init__(self, host=IP, port=PORT):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((IP, PORT))
        self.sock.listen(1)
        (client_socket, clientaddress) = self.sock.accept()
        print('Conexion desde: ', clientaddress)
        while True:
            data = client_socket.recv(1024)
            print("Cliente %s" % data) 
            new_data = str(input(">> "))
            client_socket.send(new_data.encode('utf-8'))
            if not new_data: break 
        client_socket.close()
        self.sock.close()
s = Servidor()