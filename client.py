import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
print('Соединение с сервером')

msg = '1'

while msg != 'exit':
	print('Введите сообщение:')
	msg = input()
	sock.send(msg.encode("utf-8"))
	data = sock.recv(1024)
	print("Ответ: ", data.decode("utf-8"),"\n")
sock.close()
