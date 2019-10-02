import socket
import json


def mem(ipv):
    with open('names.json', "r") as file:
        memory = json.load(file)
        if ipv not in memory:
            return False
        else:
            return memory[ipv][0]


def autoriz(ipv, passw):
    with open('names.json', "r") as file:
        memory = json.load(file)
        if memory[ipv][1] == passw:
            return True
        else:
            return False




sock = socket.socket()
port = 9090
try:
    sock.bind(('192.168.0.100', port))
except:
    port+=1
    sock.bind(('192.168.0.100', port))
sock.listen(4)
command = ("exit")


while True:
    conn, addr = sock.accept()
    print(addr)

    check = mem(addr[0])
    access = False
    if check:
        msg = f'Добрый вечер, {check}! Ваш пароль? '
        while not access:
            conn.send(msg.encode())
            passw = conn.recv(1024)
            passw = passw.decode()
            access = autoriz(addr[0], passw)
            msg = 'Неверный ввод!'
        msg = 'ДАРОВА'
        conn.send(msg.encode())

    else:
        msg = "Введите, ваше имя и пароль: "
        conn.send(msg.encode())
        name = conn.recv(1024)
        passw = conn.recv(1024)
        passw = passw.decode()
        name = name.decode()
        with open('names.json', 'r') as file:
            names = json.load(file)
            names[addr[0]] = [name, passw]
        with open ('names.json', 'w') as file:
            json.dump(names, file)
    msg = "Здесь сегодня тесновато. Но для тебя всегда место найдется!"
    conn.send(msg.encode())
    data = 'new'


    while data:
        data = conn.recv(1024)
        data = data.decode()
        if data not in command:
            print(data)
        else:
            with open("log_serv.json", "a") as file:
                json.dump(data, file)






