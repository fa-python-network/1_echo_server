import socket
from time import sleep

port = 9090
connections = {}

sock = socket.socket()
sock.bind(('', port))
print("Сервер запущен")
sock.listen(10)
sock.setblocking(0)
print("Начало прослушивания порта")

while True:
	try: 
		conn, addr = sock.accept()
	except:
		pass
	else:
		connections[conn] = conn.recv(1024).decode()
		for i in connections:
			if i != conn:
				i.send(('Новый участник: '+connections[conn]+'\n').encode())

	for conn in connections:
		conn.setblocking(0)
		try: 
			data = conn.recv(1024).decode()
		except:
			pass
		else:
			if data == 'exit':
				data = (connections.pop(conn)+' покинул нас\n')
				print(data)
				sleep(2)
				for i in connections:
					if i != conn:
						i.send(data.encode())
				break
			else:
				for i in connections:
					if i != conn:
						i.send((connections[conn]+': '+data+'\n').encode())
	sleep(1)

print('Остановка сервера')
sleep(10)
conn.close()

