import socket
import logging as l

format = '%(levelname)s %(asctime)s - %(message)s'
l.basicConfig(filename='logs.log', format=format, datefmt='%d.%m.%Y %H:%M:%S', level=l.INFO)

l.info('Start logging')

sock = socket.socket()
sock.bind(('', 9090))
l.info('порт сервера: 9090')
sock.listen(0)
l.info('Сервер работает')

while True:
    conn, addr = sock.accept()
    l.info(f'Пользователь {addr} подключен к серверу')
msg = ''

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data)
    l.info('Сервер отправляет ответ')

conn.close()
l.info('Соединение отключено')