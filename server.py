import socket
import socket
import json
import hashlib
import pickle
from loger import Logfile
from random import randint

def msgreciever(conn) ->str: #получения текстового сообщения с фиксированным заголовком
	msg_len = int(conn.recv(2), 10)
    return conn.recv(msg_len).decode()

def msgsending(conn, msg: str):   #отправкa сообщения с заголовком фиксированной длины
	msg = f"{len(msg):<{self.size}}" + msg
    conn.send(bytes(msg),"utf-8")





def identification(c,ad):
	try:
		open('users.json').close()
	except:
		open('users.json','w').close()
	with open('users.json','r', encoding="utf-8") as f:
		try:
			d = json.load(f)
			name = d[ad[0]]
			conn.send(name.encode())
			conn.send("Введите свой пароль: ".encode('utf-8'))
			passwd = conn.recv(1024).decode()
			print("Верный пароль!" if self.Pswdcheck(passwd,d[str(ad[0])]['password']) else "Неверный пароль")
		except:
			conn.send('Это неизвестный пользователь. Скажите мне ваше имя: '.encode())
			name = conn.recv(1024).decode()
			conn.send(" Придумайте себе пароль:".encode())
			passwd = HashGenerator(conn.recv(1024).decode())
			with open('users.json','w', encoding="utf-8") as g:
				json.dump({ad[0] : {'name': name, 'password': passwd} },g)
	return ("Здравствуйте,", name,"!")

def HashGenerator( pswd) -> bytes:
		 key = hashlib.md5(pswd.encode() + b'salt').hexdigest()
		 return key
			
def Pswdcheck( pswd, userk) -> bool:
		 key = hashlib.md5(pswd.encode() + b'salt').hexdigest()
		 return key == userk

l = Logfile()
l.serverstart()
try:
	port=int(input("Ваш порт:"))
	if not 0 <= port <= 65535:
		raise ValueError
except ValueError:
		port = 9090

def random_free_port(p):
	try:
		sock = socket.socket()
		sock.bind(('',p))
		sock.close
		return p
	except:
		for _ in range(0, 65536):
			try:
				p=randint(0,65535)
				sock = socket.socket()
				sock.bind(('',p))
				sock.close
				return p
			except:
				continue    
port=random_free_port(port)          
print('Номер порта:',port)
while True:
	sock = socket.socket()
	sock.bind(('', port))
	sock.listen(1)
	conn, addr = sock.accept()
	f=identification(conn,addr)
	msg = '\nconeccted'
	data=list()
	print(msg)
	while True:
		findings = conn.recv(1024)
		if findings:
				data.append(findings.decode())
				print(data[-1])
		else:
			conn.close()
			break

print('\n'.join(data))


conn.close()
l.serverend()
