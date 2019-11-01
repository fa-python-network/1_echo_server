import socket
import threading
import sys

host = socket.gethostbyname(socket.gethostname())
port = 9091

class Server:
	sock = socket.socket(socket.AF_INET,socket.SOCK_SREAM)
	connections = []

	def __init__(self):
		self.sock.bind((host,port))
		self.sock.listen(1)

	def handler(self, c, a):
		while True:
			data = c.recv(1024)
			for connection in self.connections:
				connection.send(data)
			if not data:
				self.connections.remove(c)
				c.close
				break
	def run(self):

		while true:
			c,a = self.sock.accept()
			cThread = threading.Thread(target = self.handler, args = (c,a))
			cThread.daemon = True
			cThread.start()
			self.connections.append(c)
			print(self.connections)
class Client:
	sock = socket.socket(socket.AF_INET,socket.SOCK_SREAM)
	def sendMsg(self):
		while True:
			self.sock.send(bytes(input(""), "utf-8"))
	def __init__(self, addr):
		sels.sock.connect((addr, 9090))

		iThread = threading.Thread(targe = self.sendMsg)
		iThread.daemon = True
		iThread.start()

		while True:
			data = self.sock.recv(1024)
			if not data:
				break
			print(str(data, 'utf-8')
