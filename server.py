import socket
from datetime import datetime
from contextlib import closing
import os
import hashlib
import json
from sc import SocketMethods
import pickle
from threading import Thread
import sys


class Server():

	def __init__(self,log = "file.log", users = "users.json", clients = [], status = None):
		self.__log = log
		self.__users = users
		self.clients = clients
		self.port =  int(input("Порт:"))
		self.sock = None
		self.status = status
		self.startServer()

	def startServer(self):
		self.sock = socket.socket()
		#self.port = self.check_port()
		self.sock.bind(('', self.port))
		self.sock.listen(5)
		while True:
			conn, addr = self.sock.accept()
			self.serverStarted(addr)
			Thread(target = self.listenToClient,args = (conn,addr)).start()
			self.clients.append(conn)
			#self.checkUser(addr,conn)
			# Thread(target=self.recv).start()
	# def check_port(self):
	# 	self.port = self.port if (self.port >= 0 and self.port <= 65535)  else  9090
	# 	for port in range(self.port, 65536):
	# 		try:
	# 			sock = socket.socket()
	# 			sock.bind(('',port))
	# 			sock.close
	# 			print(f"Ваш порт {self.port}")
	# 			return port
	# 		except:
	# 			pass
	# 	raise("Something went wrong")
		
			#Thread(target=self.recv).start()
			# print(self.checkUser(addr, conn))
			# self.serverStarted(addr)
	def broadcast(self,msg): 
		for sock in self.clients:
			data = pickle.dumps(["message",msg])
			sock.send(data)
	'''
	Проверка порта, который мы будем использовать на нашем
	сервере!

	'''	
	def checkPasswrd(self, passwd, userkey) -> bool:
		key = hashlib.md5(passwd.encode() + b'salt').hexdigest()
		return key == userkey

	def generateHash(self, passwd) -> bytes:
		key = hashlib.md5(passwd.encode() + b'salt').hexdigest()
		return key
	
	def listenToClient(self, conn, address):
		self.checkUser(address,conn)
		while True:
				data = conn.recv(1024)
				if data:
					status , data = pickle.loads(data)
					if status == "message":
						print(data)
						self.broadcast(data)
				else:
					conn.close()
					break

	def serverStarted(self,ip):
		with open(self.__log, "a", encoding="utf-8") as f:
			print(f"{datetime.now().time()} Server Launched {ip}", file=f)
	def serverStopped(self,ip):
		with open(self.__log, "a", encoding="utf-8") as f:
			print(f"{datetime.now().time()} Server Stopped {ip}", file = f)

	def checkUser(self, addr, conn):
		try:
			open(self.__users).close()
		except FileNotFoundError:
			open(self.__users, 'a').close()
		with open(self.__users, "r") as f:
			try:
				print("Here")
				users = json.load(f)
				name = users[str(addr[0])]['name']
				conn.send(pickle.dumps(["passwd","Введите свой пароль: "]))
				passwd = conn.recv(1024).decode()
				conn.send(pickle.dumps(["success",f"Здравствуйте, {name}"])) if self.checkPasswrd(passwd,users[str(addr[0])]['password']) else print("Incorrect")
			except:
				conn.send("Привет. Я тебя не знаю. Скажи мне свое имя: ".encode())
				name = conn.recv(1024).decode()
				conn.send("Введите свой пароль:".encode())
				passwd = self.generateHash(conn.recv(1024).decode())
				with open(self.__users, "w", encoding="utf-8") as f:
					json.dump({addr[0] : {'name': name, 'password': passwd} },f)


	'''
	успешное подключение
	'''
	# def success(self,userName, conn):
	# 	self.clients.append((userName, conn))


	'''
	отправка сообщений от пользователя к пользователю
	'''
	# def sendMessage(self,fromUser,toUser, message):
	# 	conn = None
	# 	for user in self.clients:
	# 		if user[0] == toUser:
	# 			conn = user[1]
	# 			break
	# 	if conn:
	# 		data = pickle.dumps(["message", fromUser, message])
	# 		self.sock.send(data)

	'''
	Принятие сообщений
	'''
server = Server()
