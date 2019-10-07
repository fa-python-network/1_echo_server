import socket
import random

k = open('log.txt', 'w')

sock = socket.socket()

port = 9090
try:
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

except:
    port = 9090
    k.write('некорректные данные')

f=0
while f!=1:
    try:
        sock.bind(('', port))
        f=1
    except:
        port=random.randint(1024,65535)
print('слушаю порт: ', port)

sock.listen(1)
conn, addr = sock.accept()
print(addr)

ad = addr[0]
f = open('f7.txt', 'r+')
l = [line.strip() for line in f]

if l.count(ad)==0:
	conn.send('введите ваше имя'.encode())
	name = conn.recv(1024).decode()
	l.append(ad),l.append(name)
	conn.send("привет {na}".format(na=name).encode())
	for index in l:
		f.write(index + '\n')
else:
	conn.send("привет {na}".format(na=l[l.index(ad)+1]).encode())

f.close()
msg = ''

while True:
	data = conn.recv(1024)
	if not data:
		print(msg)
		msg = ''
		sock.listen(1)
		conn, addr = sock.accept()
	msg += data.decode()
	conn.send(msg.encode())
conn.close()


