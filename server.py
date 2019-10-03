import socket
import logging as l

log_format = '%(levelname)s %(asctime)s - %(message)s'
l.basicConfig(filename='server.log', format = log_format ,datefmt='%d.%m.%Y %H:%M:%S', level=l.INFO)

l.info('Start logging INFO')


sock = socket.socket()
sock.bind(('', 9090))
l.info ('Сервер подключился к порту: 9090')
sock.listen(0)
conn, addr = sock.accept()
print(addr)
l.info('Сервер ожидает подключения...')

msg = ''

while True:
   data = conn.recv(1024)
   if not data:
       break
   msg += data.decode()
   conn.send(data)
    conn, addr = sock.accept()
    l.info(f'Клиент {addr} подключился к серверу')
    msg = ''

print(msg)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.send(data)
        l.info ('Сервер отправляет ответ клиенту')


conn.close()
    conn.close()
    l.info('Соединение завершено')
