import socket
from time import sleep

sock = socket.socket()
sock.bind(('', 9090))
print("Сервер запущен")
sock.listen(1)
print("Начало прослушивания порта")
conn, addr = sock.accept()
print("Клиент ", addr," подключился.")

msg = ''

while True:
	data = conn.recv(1024)
	print("Прием данных")
	if not data:
		print("Клиент разорвал соединение")
		break
	msg += data.decode("utf-8")
	conn.send(data)
	print("Отправка данных")

print('Остановка сервера')
sleep(10)

conn.close()
