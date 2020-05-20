import socket
from time import sleep

sock = socket.socket()

client_host = input('Введите имя хоста: ')
if client_host == 'localhost':
    pass
else:
    if any(c.isalpha() for c in client_host) == True:
        print('некорректный хост. По умолчанию локальный хост')
        client_host = 'localhost'
    else:
        host_lst = client_host.split('.')
        for i in host_lst:
            if 0 <= int(i) <= 255:
                pass
            else:
                client_host = 'localhost'
                print('Введено некорректный хост. По умолчанию локальный хост')

try:
    port = int(input('номер порта: '))
    if 0 <= port <= 65535:
        pass
    else:
        print('некорректный порта. порт по умолчанию 9020')
        port = 9020

except ValueError:
    print("Некорректный порта. по умолчанию 9020")
    port = 9020

sock.connect((client_host, port))

print('exit для завершения работы с сервером')
msg = ''