import socket
from datetime import datetime
from contextlib import closing
class Server():
	def __init__(self, log = "file.log"):
		self.__log = log
		self.port =  int(input("Порт:"))
	@property
	def startServer(self):
		self.port = self.check_port()
		print(f"Ваш порт {self.port}")
		while True:
			sock = socket.socket()
			sock.bind(('', self.port))
			sock.listen(1)
			conn, addr = sock.accept()
			self.serverStarted(addr)
			data=list()
			while True:
				msg = conn.recv(1024)
				if msg:
					data.append(msg.decode())
					print(data[-1])
				else:
					conn.close()
					self.serverStopped(addr)
					break

	def check_port(self):
		self.port = self.port if (self.port >= 0 and self.port <= 65535)  else  9090
		for port in range(self.port, 65536):
			try:
				sock = socket.socket()
				sock.bind(('',port))
				sock.close
				return port
			except:
				pass
		assert False, "Порт не найден"
	def serverStarted(self,ip):
		with open(self.__log, "a", encoding="utf-8") as f:
			print(f"{datetime.now().time()} Server Launched {ip}", file=f)
	def serverStopped(self,ip):
		with open(self.__log, "a", encoding="utf-8") as f:
			print(f"{datetime.now().time()} Server Stopped {ip}", file = f)
server = Server()
server.startServer