import socket
from time import sleep

host = input('Введите хост: ')
while True:
	port = input('Введите порта: ')
	try:
		port = int(port)
		if 100 <= port <= 65535:
			break
		print("Неправильный диапазон")
	except ValueError:
		print("Неправильный порт")
		
sock = socket.socket()
sock.setblocking(1)
sock.connect((host, port))

msg = ""
while True:
	request_msg = input("Введите сообщение: ")
	if request_msg == "exit":
		break
	else:
		msg += "\n" + request_msg
	
sock.send(msg.encode())

data = sock.recv(1024)

sock.close()

print(data.decode())
