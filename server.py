import socket
from datetime import datetime
class serv():
    def __init__(self, log = "log.txt"):
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
    def server(self):
    	self.startserv()
    	while True:
    		sock = socket.socket()
    		sock.bind(('', self.p))
    		sock.listen(1)
    		conn, addr = sock.accept()
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
    	self.stopserv()
S = serv()
S.server()
