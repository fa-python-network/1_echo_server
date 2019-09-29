import socket

sock = socket.socket()
sock.setblocking(1)
sock.connect(('localhost', 9090))

msg = ""
while True:
	cl_input = input()
	if cl_input == "exit":
		break
	msg += cl_input + " "
sock.send(msg.encode())

print('Receiving data from server...')
data = sock.recv(1024) #получаем ответ от сервера

print('Disconnecting..')
sock.close() #отключаемся от сервера


print(data.decode()) #выводим ответ сервера
