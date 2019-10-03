import socket
import logging as log


log.basicConfig(filename='client.txt', level=log.DEBUG)

sock = socket.socket()
log.info('Клиент запущен')
sock.connect(('localhost', 23))
log.info('Подключено к серверу')
msg = ''
while msg != 'exit':
    msg = input()
    log.info('Отправляю сообщение {}'.format(msg))
    sock.send(msg.encode())
    log.info('Получаю ответ сервера')
    received_msg = sock.recv(1024)
    print(received_msg.decode())
sock.close()
