#8 task

import socket

sock = socket.socket()

port=8089

sock.bind(("", port))
print("Server is starting")

sock.listen(1)
print("Listening client")

while True:
	conn,addr = sock.accept()

	name=""

	with open('base_client.txt', 'r+') as file:
		for line in file:
			if addr[0] in line:
				line=line.split(":")
				name = line[1]
				password = line[2]
				break


		if name!="":
			mes1="enter your password"
			conn.send(mes1.encode())
			data = conn.recv(1024)
			passwd = data.decode()
			if str(password) == str(passwd):
				mes2 = "Correct password"
				conn.send(mes2.encode())
			else:
				mes3= "Incorrect password"
				conn.send(mes3.encode())

		else:
			mes_name = "Enter your name"
			conn.send(mes_name.encode())
			newname = conn.recv(1024).decode()
			mes_passwd = "Enter your password"
			conn.send(mes_passwd.encode())
			newpasswd = conn.recv(1024).decode()
			file.write(f"{addr[0]}:{newname}:{newpasswd}:\n")
			file.close()

print(f"Connecting to client {addr}")

print("Geeting message from client")

msg=''
while True:
	data = conn.recv(1024)
	if not data:
		break
	msg+=data.decode()

print("Turn off")
conn.close()


