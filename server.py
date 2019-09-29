import socket

f = open ('log.txt', 'w')
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
print("Server starts", file = f)
sock.listen(0)
print("Now listen", file = f)
conn, addr = sock.accept()
print(addr)

msg = ''

while True:
	data = conn.recv(1024)
	print("new data from client", file = f)
	if not data:
		break
	msg += data.decode()
	conn.send(data)
	print("data to client", file = f)

print(msg)

conn.close()
print('stop client', file = f)