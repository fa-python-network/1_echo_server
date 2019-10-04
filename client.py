import socket

sock = socket.socket()
sock.setblocking(1)


host = input("Введите адрес хоста или lh: ")
if host == "lh":
	host = 'localhost'
else:
	host_ls = host.split(".", 4)
	for i in host_ls:
		if 0 <= int(i) <= 255:
			pass
		else:
			host = 'localhost'
port = int(input("Введите адрес порта: "))
if 1024 <= int(port) <= 65535:
	pass

sock.connect((host, port))

srv1 = sock.recv(1024).decode()
print(srv1)

if str(srv1) == str("Enter your name:"):
	sock.send(input().encode())
else:
	pass

print('Введите Ваше сообщение или "exit" для выхода: ')

msg = ""
while True:
	cl_input = input()
	if cl_input == "exit".strip():
		a = 1
		break
	msg += cl_input + " "
sock.send(msg.encode())

print('Receiving data from server...')

if (a == 1) and (msg == ''):
	print('Disconnecting...')
	sock.close() #отключаемся от сервера
else:
	data = sock.recv(1024) #получаем ответ от сервера

	print('Disconnecting...')
	sock.close() #отключаемся от сервера

	print(data.decode()) #выводим ответ сервера
