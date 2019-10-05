import socket
import logging as log


log.basicConfig(filename='client.txt', level=log.DEBUG)


def send(conn, message):
    header = len(message)
    full_message = f'{header:4}{message}'.encode()
    conn.send(full_message)


def receive(conn):
    header = conn.recv(4).decode()
    message = conn.recv(int(header))
    return message.decode()

sock = socket.socket()
log.info('Клиент запущен')
sock.connect(('localhost', 1427))
log.info('Подключено к серверу')
msg = ''
while msg != 'exit':
    msg = input()
    log.info('Отправляю сообщение {}'.format(msg))
    send(sock, msg)
    log.info('Получаю ответ сервера')
    received_msg = receive(sock)
    print(received_msg)
sock.close()
