import socket, re
from time import sleep

sock = socket.socket()

try:
	name_port = input("Введите имя хоста: ")
	assert re.match(r'[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}', name_port) or name_port == "localhost","Имя порта не котируется."
except (AssertionError, TypeError, ValueError) as e:
	print("Имя порта по умолчанию localhost")
	name_port = "localhost"

try:
	num_port = int(input("Введите номер порта: "))
	assert 1024 < num_port < 65535, "Введенный порт рекомендуется не использовать или он занят."
except (AssertionError, TypeError, ValueError) as e:
	print("Будет введен порт по умолчанию 9091")
	num_port = 9091

sock.connect((name_port, num_port))
print("Успешно!")
msg = 0 
inf = sock.recv(1024)
print(inf.decode())
while msg!= "exit" and "Мы с тобой не знакомы" not in inf.decode():
	msg = input()
	sock.send(msg.encode())

	inf = sock.recv(1024)
	print(inf.decode())

sock.close()


