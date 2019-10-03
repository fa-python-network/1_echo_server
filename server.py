import socket
import logging as l

log_format = '%(levelname)s %(asctime)s - %(message)s'
l.basicConfig(filename='server.log', format = log_format ,datefmt='%d.%m.%Y %H:%M:%S', level=l.INFO)
l.info('Start logging INFO')

port = 9090

sock = socket.socket()

while True:
    try:
        sock.bind(('', port))
        break
    except:
        l.info(f'Порт {port} занят')
        port += 1
        
l.info (f'Сервер подключился к порту: {port}')
sock.listen(0)
l.info('Сервер ожидает подключения...')


while True:
    conn, addr = sock.accept()
    l.info(f'Клиент {addr} подключился к серверу')
    msg = ''

    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.send(data)
        l.info ('Сервер отправляет ответ клиенту')
        

    conn.close()
    l.info('Соединение завершено')
