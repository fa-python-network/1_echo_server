import socket

sock = socket.socket()
while True:
	host = input('Введите адрес хоста или localhost : \n')
	if host=='localhost':
		host='127.0.0.1'
		break
	host_l=host.split('.')
	if (0<int(host_l[0])<255) and (0<int(host_l[1])<255) and (0<int(host_l[2])<255) and (0<int(host_l[3])<255):
		break
	else:
		print('Введен неверный формат адреса.')
while True:
	port=input('Введите номер порта от 1024 до 49151: \n')
	if 1023<int(port)<49152:
		break
	else:
		print('Неверный номер порта.')
		break
sock.bind(('', int(port)))
sock.listen(1)


while True:
	conn, addr = sock.accept()
	print("Подключение к ", addr)
	while True:
		msg=conn.recv(1024)
		if msg.decode()=='exit':
			conn.send(b"bye!")
			break
		conn.send(b"Accepted, write on")
		print(msg.decode())
	conn.close()
		

	#data = conn.recv(1024)
	#if data.decode()=='exit':
	#	break
	#msg += data.decode()
	#conn.send(data)

#print(msg)


