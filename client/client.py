import socket
from time import sleep
import json

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

def sing_in(sock):
    comand = input("Если у вас есть аккаунт введите 1, если нет то 0\n")
    if comand == '0':
        login = input('Придумайте и введите логин\n')
        passwod = input('Придумайте и введите пароль\n')
        name = input('Введите ваше имя\n')
        req = {
            "comand": "1",
            "User": {
                "login": login,
                "pass": passwod,
                "name": name,
            }
        }
        req_str = json.dumps(req)
        sock.send(req_str.encode())
        server_req = sock.recv(1024)
        server_req = server_req.decode()
        server_req = json.loads(server_req)
        print(name + ', поздравляем вы зарегистрированы!\n Ожидаем сообщений')
        return server_req['tok'], server_req['user']
    else:
        while True:
            login = input('Введите логин\n')
            passwod = input('Введите пароль\n')
            req = {
                "comand": "2",
                "User": {
                    "login": login,
                    "pass": passwod,
                }
            }
            req_str = json.dumps(req)
            sock.send(req_str.encode())
            server_req = sock.recv(1024)
            server_req = server_req.decode()
            server_req = json.loads(server_req)
            if server_req['tok'] == "":
                print('Не верный логин или пароль!')
                continue
            else:
                print(login + ', вы вошли в систему!\n Ожидаем сообщений')
                return server_req['tok'], server_req['user']

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

try:
    file = open('client/touken.txt')
    touk = file.read()
    if touk == "":
        raise ValueError
    req = {
            "comand": "3",
            "tok": touk
        }
    sock.send(json.dumps(req).encode())
    i_am = sock.recv(1024)
    i_am = i_am.decode()
    i_am = json.loads(i_am)
    print('Добро пожаловать ', i_am['Name'], ".\n Ожидаем сообщений")

except:
    r = open('client/touken.txt', 'w')
    tok, User = sing_in(sock)
    r.write(tok)
    r.close()


input_date = input()
while input_date != "exit":
    msg += input_date
    input_date = input()

if msg != "":
    sock.send(msg.encode())
    data = sock.recv(1024)
    print(data.decode())

sock.close()
