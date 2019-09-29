import socket

sock = socket.socket()
while True:
    port = input('Введите порт от 1024 до 65535: \n')
    if not port.isnumeric():
        print('Ошибка')
    elif 1023 <= int(port) <= 65535:
        break
    else:
        print('Ошибка: порт не входит в нужный диапазон')
sock.bind(('', int(port)))
sock.listen(0)
conn, addr = sock.accept()
print(addr)

msg = ''

while True:
	data = conn.recv(1024)
	if not data:
		break
	msg += data.decode()
	conn.send(data)

print(msg)

conn.close()
