import socket

sock = socket.socket()
HOST = ''
PORT = 8086

sock.bind((HOST, PORT))

print('Сервер запускается, немного терпения!')
print('Начинаем слушать порт...')

sock.listen(1)
conn, addr = sock.accept()
print('Готов к обмену данными с клиентом')

msg = ''
while True:
	data = conn.recv(1024)
	if not data:
		break
	else:
		msg += data.decode()
		conn.send(data.decode().upper().encode())

print(msg, sep=' ') #хотел через sep сделать разделитель, но почему то не пошло!
conn.close()