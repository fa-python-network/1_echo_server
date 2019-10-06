import socket

sock = socket.socket()

port = 9090
print('выбран порт:', port, 'изменить? Y/N')
f = input()
if f.upper() == 'Y':
	q = 0
	while q==0:
		port = int(input('введите номер порта: '))
		if port>=1024 and port<=65535:
			q = 1
		else:
			print('некорректные данные, повторите ввод')

sock.bind(('', port))
sock.listen(0)
conn, addr = sock.accept()
print(addr)

msg = ''

while True:
	data = conn.recv(1024)
	if not data:
		print(msg)
		msg = ''
		sock.listen(0)
		conn, addr = sock.accept()
	msg += data.decode()
	conn.send(msg.encode())
print(msg)
conn.close()
