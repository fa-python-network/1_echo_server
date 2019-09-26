import socket
from time import sleep

sock = socket.socket()
sock.setblocking(True)
p = int(input("Your port:"))
p = p if (p >= 1024 and p <= 65535) else None #Сервера с портом меньше чем 1024 априори не существует (Поставлено условие в server.py). Клиента вырубит автоматически.
sock.connect((input("Your host:"), p))

msg = input()
#msg = "Hi!"
while True:
	if msg != "rabbit":
		sock.send(msg.encode())
		msg = input()
	else:
		break

sock.close()