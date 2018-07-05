import socket
import threading
import sys
import pickle

IP = "localhost"
PORT = 8080

class Cliente():
	
	def __init__(self, host=IP, port=PORT):
		
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((IP, PORT))

		recv = threading.Thread(target=self.recv)
		recv.daemon = True
		recv.start()

		while True:
			msg = input('->')
			if msg != 'salir':
				self.send(msg)
			else:
				self.sock.close()
				sys.exit()

	def recv(self):
		while True:
			try:
				data = self.sock.recv(1024)
				if data:
					print(pickle.loads(data))
			except:
				pass

	def send(self, msg):
		self.sock.send(pickle.dumps(msg))

c = Cliente()