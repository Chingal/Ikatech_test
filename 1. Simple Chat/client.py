#!/usr/bin/env python
import socket

IP = "localhost"
PORT = 8081

class Cliente():
	def __init__(self, host=IP, port=PORT):
		self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.client_socket.connect((IP, PORT))
		while True:
			data = str(input(">> "))
			self.client_socket.send(data.encode('utf-8'))
			if not data: break 
			new_data = self.client_socket.recv(1024) 
			print('Servidor: %s' % new_data) 
		self.client_socket.close()

client = Cliente()