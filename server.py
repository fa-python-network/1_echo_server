import socket
from re import match

sock = socket.socket()
print('Запуск сервера')
host = 'localhost'
port = 135  # 9090
host_ = input('Host: ')
port_ = input('Port:')
host_regex = r'[0-2]?[0-9]?[0-9]\.[0-2]?[0-9]?[0-9]\.[0-9]?[0-9]?[0-9]\.[0-2]?[0-9]?[0-9]'
if host_ and match(host_regex, host_):
    host = host_
print(f'current host:{host}')
if port_.isdigit() and 1024 <= int(port_) <= 65535:
    port = int(port_)

try:
    sock.bind(('', port))
except OSError:
    sock.bind(('', 0))
    port = sock.getsockname()[1]

print('Сервер слушает порт {}'.format(port))
print(f'current port: {port}')
sock.listen(5)

try:
    while 1:
        conn, addr = sock.accept()
        print('Подключен клиент {}:{}'.format(*addr))
        while 1:
            received_msg = conn.recv(1024).decode()
            conn.send(received_msg.encode())
            if not received_msg:
                print('Разрыв соединения')
                conn.close()
                break

finally:
    print('Сервер завершает работу')
    sock.close()
