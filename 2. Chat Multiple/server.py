import socket
import threading
import sys
import pickle

IP = "localhost"
PORT = 8080

class Servidor():
	
	def __init__(self, host=IP, port=PORT):
		self.clientes = []

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((IP, PORT))
		self.sock.listen(10)
		self.sock.setblocking(False)

		add = threading.Thread(target=self.add_client)		
		add.daemon = True
		add.start()

		emmit = threading.Thread(target=self.emmit)
		emmit.daemon = True
		emmit.start()

		while True:
			msg = input('->')
			if msg == 'salir':
				self.sock.close()
				sys.exit()
			else:
				pass


	def add_client(self):
		print("Add Client...")
		while True:
			try:
				conn, addr = self.sock.accept()
				conn.setblocking(False)
				self.clientes.append(conn)
			except:
				pass

	def emmit(self):
		print("Emitiendo...")
		while True:
			if len(self.clientes) > 0: # Si hay clientes 
				for cl in self.clientes: # Se recorre la lista de clientes
					try:
						data = cl.recv(1024)
						if data:
							self.broadcast(data,cl)
					except:
						pass
	
	def broadcast(self, msg, cliente):
		for cl in self.clientes:
			try:
				if cl != cliente:
					cl.send(msg)
			except:
				self.clientes.remove(cl)

s = Servidor()