import socket
sock = socket.socket()
import random
from threading import Thread 
connected_users = []


def new_client(conn, addr):
	strok = str(addr[0])
	passwd0 = conn.recv(128)
	passwd = str(passwd0.decode()) + '\n'
	with open('address_log.txt', 'r', encoding = 'utf-8') as file:
		for line in file:
			line1 = line.split(';')
			if strok == line1[0] and passwd == line1[1]:
				print("Hello, dude ", addr[0])
				break
		else:
			print("nevernuy parol ili novuy user")
				
	with open('address_log.txt', 'a', encoding = 'utf-8') as file:
		file.write(str(addr[0]) + ';' + str(passwd))
	with open('server_log.txt', 'a', encoding = 'utf-8') as file:
		file.write(str(addr) + '  ' + 'connected\n')
	while True:
		data = conn.recv(1024)
		if not data:
			break
		msg = data.decode()
		if msg != 'client disconnected':
			print(addr, msg)
			for user in connected_users:
				if conn != user:
					po = str(addr) + str(msg)
					user.send(po.encode())
		else:
			with open('server_log.txt', 'a', encoding = 'utf-8') as file:
				file.write(str(addr) + '  ' + 'disconnected\n')
				try:
					connected_users.remove(conn)
				except:
					break
		
	conn.close()


try:
	port = 9095
	sock.bind(('', port))
except:
	port = random.randint(1024,65535)
	sock.bind(('', port))
sock.listen(0)
print("port№", port)

msg = ''
while True:
	conn, addr = sock.accept()
	connected_users.append(conn)
	Thread(target=new_client, args=(conn, addr)).start()
