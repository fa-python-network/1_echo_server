import socket

sock = socket.socket()

while True:
	file=open('server.log','a')
	host = input('Введите адрес хоста или localhost или пропустите этот шаг, нажав Enter: \n')
	file.write("Запрашиваю адрес хоста...\n")
	if host=='localhost':
		host='127.0.0.1'
		file.write(f"введенный адрес хоста: {host} \n")
		file.close()
		break
	if host=='':
		file.write("адрес хоста не установлен. \n")
		file.close()
		break
	host_l=host.split('.')
	if (0<int(host_l[0])<255) and (0<int(host_l[1])<255) and (0<int(host_l[2])<255) and (0<int(host_l[3])<255):
		file.write(f"Введенный адрес хоста: {host} \n")
		file.close()
		break
	else:
		print('Введен неверный формат адреса.')
		file.write("Введен неверный адрес хоста, запрашиваю адрес снова.\n")


while True:
	file=open('server.log','a')
	port=input('Введите номер порта от 1024 до 49151: \n')
	port=int(port)
	file.write("Запрашиваю номер порта...\n")
	if 1023<port<49152:
		file.write(f"введенный номер порта: {port} \n")
		file.close()
		break
	else:
		print('Неверный номер порта.')
		file.write("введен неверный номер порта, запрашиваю номер снова...\n")
while True:
	try:
		sock.bind(('', port))
		break
	except:
		if 1023<port<=49150:
			port+=1
		else:
			port=9090

sock.listen(1)
print(f'Слушаю порт {port}.')
while True:
	file=open('server.log','a')
	conn, addr = sock.accept()
	print("Подключение к ",addr)
	file.write(f"Подключение к  {addr} \n")
	file.close()
	while True:
		file=open('server.log','a')
		msg=conn.recv(1024)
		if msg.decode()=='exit':
			file.write(f"Попращался с {addr}. \n \n \n")
			conn.send(b"bye!")
			file.close()
			break
		conn.send(b"Accepted, write on")
		file.write(f"Принял сообщение {msg} от {addr}, жду следующее. \n")
		print(msg.decode())
		file.close()
	conn.close()

		

	#data = conn.recv(1024)
	#if data.decode()=='exit':
	#	break
	#msg += data.decode()
	#conn.send(data)

#print(msg)


