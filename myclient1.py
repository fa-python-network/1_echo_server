# 8 task

import socket

sock = socket.socket()

port=8089

sock.connect(("", port))

data = sock.recv(1024).decode()
print(data)
if "enter your password" in data:
	password=input()
	sock.send(password.encode())
	ans = sock.recv(1024)
	print(ans.decode())

elif "Enter your name" in data:
	name=input()
	sock.send(name.encode())
	ans1 = sock.recv(1024)
	print(ans1.decode())
	if "Enter your password" in ans1.decode():
		passwd=input()
		sock.send(passwd.encode())
		ans2 = sock.recv(1024)
		print(ans2.decode())

