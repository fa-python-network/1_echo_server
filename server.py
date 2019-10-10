import socket
from datetime import datetime
from contextlib import closing
import os
import hashlib
import json
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
		while True:	
 			try:	
 				self.sock.bind(('',self.port))	
 				break
 			except:
 				self.port+=1		
		print(f'Занял порт {self.port}')
		self.sock.listen(5)
		while True:
			conn, addr = self.sock.accept()
			self.serverStarted(addr)
			Thread(target = self.listenToClient,args = (conn,addr)).start()
			self.clients.append(conn)

	def broadcast(self,msg, conn): 
		for sock in self.clients:
			if sock != conn:
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
						self.broadcast(data, conn)
				else:
					conn.close()
					self.clients.remove(conn)
					self.serverStopped(address)
					break

	def serverStarted(self,ip):
		with open(self.__log, "a", encoding="utf-8") as f:
			print(f"{datetime.now().time()} Server Launched {ip}", file=f)
	def serverStopped(self,ip):
		with open(self.__log, "a", encoding="utf-8") as f:
			print(f"{datetime.now().time()} Server Stopped {ip}", file = f)

	def checkUser(self, addr, conn):
		try:		екнЖ

			open(self.__users).close()
		except FileNotFoundError:
			open(self.__users, 'a').close()
		with open(self.__users, "r") as f:
			try:
				users = json.load(f)
				name = users[str(addr[0])]['name']
				conn.send(pickle.dumps(["passwd","Введите свой пароль: "]))
				passwd = pickle.loads(conn.recv(1024))[1]
				conn.send(pickle.dumps(["success",f"Здравствуйте, {name}"])) if self.checkPasswrd(passwd,users[str(addr[0])]['password']) else self.checkUser(addr,conn)
			except:
				conn.send(pickle.dumps(["auth",f"Привет. Я тебя не знаю. Скажи мне свое имя: "]))
				name = pickle.loads(conn.recv(1024))[1]
				conn.send(pickle.dumps(["passwd","Введите свой пароль: "]))
				passwd = self.generateHash(pickle.loads(conn.recv(1024))[1])
				conn.send(pickle.dumps(["success",f"Здравствуйте, {name}"]))
				with open(self.__users, "w", encoding="utf-8") as f:
					json.dump({addr[0] : {'name': name, 'password': passwd} },f)

server = Server()
