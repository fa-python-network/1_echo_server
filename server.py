import socket
import json
import logging as l


log_format = '%(levelname)s %(asctime)s - %(message)s'
l.basicConfig(filename='server.log', format = log_format ,datefmt='%d.%m.%Y %H:%M:%S', level=l.INFO)
l.info('Start logging INFO')

port = 9090

sock = socket.socket()


def check(host_name):
    with open('user.json', "r") as file:
        user_d = json.load(file)
        if host_name in user_d:
            return user_d[host_name]
        else:
            return False


while True:
    try:
        sock.bind(('', port))
        break
    except:
        l.info(f'Порт {port} занят')
        port += 1

l.info (f'Сервер подключился к порту: {port}')
print (f'Сервер подключился к порту: {port}')
sock.listen(0)
l.info('Сервер ожидает подключения...')



while True:
    conn, addr = sock.accept()
    l.info(f'Клиент {addr} подключился к серверу')
    msg = ''

    ch = check(addr[0])
    if ch:
        msg = f'Здравствуйте, {ch}!'
        conn.send(msg.encode())
    else:
        msg = 'Пожалуйста, введите ваше имя:'
        conn.send(msg.encode())
        name = conn.recv(1024)
        name = name.decode()
        with open('user.json', 'r') as file:
            users = json.load(file)
            users[addr[0]] = name                  
        with open ('user.json', 'w') as file:
            json.dump(users, file)
            msg = f"Здравствуйте, {name}"
            conn.send(msg.encode())

    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.send(data)
        l.info ('Сервер отправляет ответ клиенту')

            

    conn.close()
    l.info('Соединение завершено')
