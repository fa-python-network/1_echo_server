import socket

sock = socket.socket()
f=open('log_file_server', 'a')

port = int(input('Введите номер порта:'))
if (1023 < port < 49152):
    f.write('Клиент ввел номер порта: {port} \n')
    break
else:
    port = 9090
    f.write('Клиент ввел неверный номера порта. Порту автоматически присвоен номер {port}')

while True:
	try:
		sock.bind(('', port))
		break
	except:
		if port > 49151:
			port = 9090
		else:
			port += 1
            
sock.listen(1)
print('Слушаю порт с номером {port}')
f.write('\nСлушаю порт..\n')

while True:
    f=open('log_file_server', 'a')
    conn, addr = sock.accept()
	data = conn.recv(1024)
    f.write('Подключился клиент с {addr}\n')
    
    while True:
    	if data.decode() == 'exit':
            f.write('{addr} отключился\n')
    		break
   
	conn.send(data)
    f.write('Отправляю данные {addr}\n')
    print(msg.decode())
    f.close()

conn.close()
f.close()