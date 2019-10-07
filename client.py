import socket

sock = socket.socket()
try:
    print('Введите ip: ')
    ip = input()
    print('Введите port: ')
    port = int(input())
    sock.connect((ip, port))
    print('Соединение с сервером.')
    
    msg=input()
    while msg!='exit':
        
        sock.send(msg.encode())
        data = sock.recv(1024)
        print('Отправка данных серверу')
        msg=input()
    
except:
    print('Разрыв соединения с сервером.')
    sock.close()

sock.close()