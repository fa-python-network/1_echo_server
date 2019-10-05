import socket
from datetime import datetime
from contextlib import closing
import os
import json
class Server():
	def __init__(self, log = "file.log", users = "users.json"):
		self.__log = log
		self.__users = users
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
			print(self.checkUser(addr, conn))
			self.serverStarted(addr)
			data = list()
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
	
	def checkUser(self, addr, conn):
		try:
			open(self.__users).close()
		except FileNotFoundError:
			open(self.__users, 'a').close()
		with open(self.__users, "r") as f:
			try:
				users = json.load(f)
				name = users[str(addr[0])]['name']
				conn.send("Введите свой пароль: ".encode('utf-8'))
				passwd = conn.recv(1024).decode()
			except KeyError:
				conn.send("Привет. Я тебя не знаю. Скажи мне свое имя: ".encode())
				name = conn.recv(1024).decode()
				conn.send("Введите свой пароль:".encode())
				passwd = conn.recv(1024).decode()
				with open(self.__users, "w", encoding="utf-8") as f:
					json.dump({addr[0] : {'name': name, 'password': passwd} },f)
		return f"Здравствуйте, {name}"
	def serverStarted(self,ip):
		with open(self.__log, "a", encoding="utf-8") as f:
			print(f"{datetime.now().time()} Server Launched {ip}", file=f)
	def serverStopped(self,ip):
		with open(self.__log, "a", encoding="utf-8") as f:
			print(f"{datetime.now().time()} Server Stopped {ip}", file = f)
server = Server()
server.startServer
