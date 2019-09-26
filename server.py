import socket
from datetime import datetime

class Server():
	def __init__(self, log = "file.log"):
		self.__log = log
		self.port =  int(input("Порт:"))
		self.port = self.port if (self.port >= 0 and self.port <= 65535)  else  9090
	@property
	def startServer(self):
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
	def serverStarted(self,ip):
		with open(self.__log, "a", encoding="utf-8") as f:
			print(f"{datetime.now().time()} Server Launched {ip}", file=f)
	def serverStopped(self,ip):
		with open(self.__log, "a", encoding="utf-8") as f:
			print(f"{datetime.now().time()} Server Stopped {ip}", file = f)
server = Server()
server.startServer