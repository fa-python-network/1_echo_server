import socket



sock = socket.socket()
print('Клиент запущен')
port = 8564
sock.bind(('', port)) 
print('Подключено к серверу')
msg = ''
while msg != 'exit':
    msg = input()
    print('Отправляю сообщение {}'.format(msg))
    sock.send(msg.encode())
    print('Получаю ответ сервера')
    received_msg = sock.recv(1024)
    print(received_msg.decode())
sock.close()

