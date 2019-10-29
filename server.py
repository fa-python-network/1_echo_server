f = open('Log.txt', 'a')
f.write("Запуск сервера")
import socket

i = 1024
sock = socket.socket()
while true:
	while i < 2 ** 16:
		try:
			i = i+1;
			sock.bind(('', i))
			break
		except:
			pass
			

	f.write("порт = ", i)
	f.write("Начало прослушивание порта")
	sock.listen(1)
	conn, addr = sock.accept()
	print(addr)

	msg = ''

	f.write("Прием данных от клиент")
	while True:
		data = conn.recv(1024)
		if not data:
			break
		msg += data.decode()
		f.write("Отправка данных клиенту")
		conn.send(data)

	f.write("Отключение клиента")
	print(msg)

f.write("отключение сервера")
conn.close()
