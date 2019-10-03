import socket

sock = socket.socket()
sock.connect(('localhost', 9090))

while True:
    msg = input()
    if msg == 'exit':
        break
    sock.send(msg.encode()) #отправить ответ

    data = sock.recv(1024) #получить ответ
    
    print(data.decode()) #вывод сообщения

    sock.close()


