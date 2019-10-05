import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)

while True:
	print("Выберите порт")
	port=int(input())
	if 1024<=port<=65535:
		break
	print("Ошибка, попробуйте снова")

while True:
	print("Выберите IP")
	ip=input()
	if ip =="localhost":
		break
	else:
		ip_=ip.split(".")
	count=0
	for i in ip_:
		if 0<=int(i)<=255:
			count=count+1
		if count==4:
			break	
	print("Ошибка, попробуйте снова")


sock.connect((ip, port))

print("Введите сообщение. Для выхода введите exit: ")

msg = ""

while True:
	input_ = input()
	if input_ == "exit".strip():
		count_ = 1
		break
	msg += input_ + " "
sock.send(msg.encode())
print('Отключение')
if (count_ != 1) and (msg != ''):
	data = sock.recv(1024)
	sock.close()
	print(data.decode())
else:
	sock.close()

