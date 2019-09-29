import socket

sock = socket.socket()
sock.setblocking(1)


host = input("Введите адрес хоста: ")
if host == "localhost":
	pass
else:
	hostls = host.split(".", 4)
	for i in hostls:
		if 0 <= int(i) <= 255:
			pass
		else:
			host = 'localhost'
port = int(input("Введите адрес порта: "))
if 1024 <= int(port) <= 65535:
	pass
else:
	port = 9000

sock.connect((host, port))

msg = ""
while True:
	cl_input = input()
	if cl_input == "exit":
		break
		sock.close
	msg += cl_input + " "
sock.send(msg.encode())

print('Receiving data from server...')
data = sock.recv(1024) #получаем ответ от сервера

print('Disconnecting..')
sock.close() #отключаемся от сервера


print(data.decode()) #выводим ответ сервера
