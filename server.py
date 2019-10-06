import socket
import random
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
    print('некорректные данные')

f=0
while f!=1:
    try:
        sock.bind(('', port))
        f=1
    except:
        port=random.randint(1024,65535)
print('слушаю порт: ', port)

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
