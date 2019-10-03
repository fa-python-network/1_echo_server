import socket
from datetime import datetime
from random import randint
class serv():
    def __init__(self, log = "log.txt", user = "user.txt"):
    	self.__user = user
    	self.__logfile=log
    	self.p = int(input("Your port:"))
    	self.p = self.p if (self.p >= 1024 and self.p <= 65535) else print("Error") #Kick sistem port 
    def startserv(self):
    	with open(self.__logfile, "a", encoding="utf-8") as f:
    		print(f"{datetime.now().time()} Server Started", file=f)
    def newuser(self, ip):
    	with open(self.__logfile, "a", encoding="utf-8") as f:
    		print(f"{datetime.now().time()} Hooray, new User: {ip}!!!", file=f)
    def newmessage(self, text):
    	with open(self.__logfile, "a", encoding="utf-8") as f:
    		print(f"{datetime.now().time()} Wow, new message: {text}!", file=f)
    def kickuser(self, ip):
    	with open(self.__logfile, "a", encoding="utf-8") as f:
    		print(f"{datetime.now().time()} Kick this User: {ip}.", file=f)
    def stopserv(self):
    	with open(self.__logfile, "a", encoding="utf-8") as f:
    		print(f"{datetime.now().time()} Server Stopted", file=f)
    def rand_port(self):
    	try:
    		sock = socket.socket()
    		sock.bind(('', self.p))
    		sock.close()
    		print("Standart Port is Ready.")
    		return self.p
    	except:
    		for i in range (1024, 65536):
    			try:
    				self.p = randint(1024,65535)
    				sock = socket.socket()
    				sock.bind(('', self.p))
    				sock.close()
    				print ("Port:", self.p)
    				return self.p
    			except: 
    				continue 
    def check(self, conn, addr):
    	try:
    		open(self.__user).close()
    	except:
    		open(self.__user, 'w').close()
    	with open(self.__user, 'r', encoding='utf-8') as file:
    		d = dict(a.rstrip().split(None, 1) for a in file)
    		try:
    			n = d[str(addr[0])]
    			conn.send("Identification completed".encode())
    		except:
    			conn.send("Who are you?".encode())
    			n = conn.recv(1024).decode()
    			with open(self.__user, 'a', encoding='utf-8') as f:
    				print(f"{str(addr[0])} {n}", file=f)
    	return "Nice to meet you"
    def server(self):
    	self.startserv()
    	while True:
    		port = self.rand_port()
    		sock = socket.socket()
    		sock.bind(('', port))
    		sock.listen(1)
    		conn, addr = sock.accept()
    		print(self.check(conn,addr))
    		self.newuser(addr)
    		novip = addr
    		data = []
    		while True:
    			msg = conn.recv(1024)
    			data.append(msg.decode())
    			if data[-1] != '':
    				print(data[-1])
    				self.newmessage(data[-1])#Я думаю стоит вывести сообщение и на экране, и в лог файле.
    			else:
    				self.kickuser(novip)
    			if not msg:
    				conn.close()
    				break
    	return self.stopserv()
S = serv()
S.server()
