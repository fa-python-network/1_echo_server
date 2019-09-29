import socket
from time import sleep


def get_port():
    port = int(input('Введите порт от 1024 до 65535: \n'))
    if 1023 < port < 65535:
        return port
    print('Не валидный порт')
    return get_port()

def get_ip():
    ip = input('Введите ip (10.10.10.10) или оставьте пусстым для значения localhost: \n')

    if ip == '':
        return 'localhost'

    ip = ip.split('.')

    if len(ip) != 4:
        print('Не валидный ip')
        return get_ip()

    ip = list(map(lambda x: int(x), ip))

    for i in ip:
        if 0 <= i <= 255:
            continue
        else:
            print('Не валидный ip')
            return get_ip()
    return '.'.join(list(map(lambda x: str(x), ip)))


sock = socket.socket()
sock.setblocking(1)


while True:
    ips = get_ip()
    port = get_port()
    try:
        print('Ожидаем соединения')
        sock.connect((ips, port))
        break
    except BaseException:
        print('Возникла ошибка соединения')
        sock.close()
        sock = socket.socket()
        sock.setblocking(1)

print('Соединение установлено')

msg = ""
input_date = input()
while input_date != "exit":
    msg += input_date
    input_date = input()

if msg != "":
    sock.send(msg.encode())
    data = sock.recv(1024)
    print(data.decode())

sock.close()
