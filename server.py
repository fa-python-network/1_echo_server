print("Запуск сервера")
import socket

sock = socket.socket()
sock.bind(('', 9089))
print("Начало прослушивание порта")
sock.listen(1)
conn, addr = sock.accept()
print(addr)

msg = ''

print("Прием данных от клиент")
while True:
	data = conn.recv(1024)
	if not data:
		break
	msg += data.decode()
	print("Отправка данных клиенту")
	conn.send(data)

print("Отключение клиента")
print(msg)

print("отключение сервера")
conn.close()
