import socket
import hashlib
import json
import logging

SALT = 'memkekazaza'.encode("utf-8")

logging.basicConfig(filename="log_serv", level=logging.INFO)


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
        if memory[ipv][1] == hashpass(passw):
            return True
        else:
            return False


def hashpass(passw: str):
    return hashlib.sha512(passw.encode("utf-8") + SALT).hexdigest()


def sendmsg(who, msg):
    msg_len = str(len(msg))
    while len(msg_len) < 5:
        msg_len = '0' + msg_len
    who.send((msg_len + msg).encode())


def checkmsg(who):
    msg_len = int(who.recv(4).decode())
    msg = who.recv(msg_len).decode()
    return msg


sock = socket.socket()
port = 9090
try:
    sock.bind(('10.38.50.16', port))
except:
    port += 1
    sock.bind(('10.38.50.16', port))
sock.listen(4)
command = ("exit")


while True:
    conn, addr = sock.accept()
    logging.info(f"Connect - {addr}")

    check = mem(addr[0])
    access = False
    if check:
        msg = f'Добрый вечер, {check}! Ваш пароль? '
        while not access:
            sendmsg(conn, msg)
            passw = checkmsg(conn)
            access = autoriz(addr[0], passw)
            msg = 'Неверный ввод!'
        msg = 'ДАРОВА'
        sendmsg(conn, msg)

    else:
        sendmsg(conn, "Введите, ваше имя и пароль: ")
        name = checkmsg(conn)
        passw = checkmsg(conn)

        with open('names.json', 'r') as file:
            names = json.load(file)
            names[addr[0]] = [name, hashpass(passw)]
        with open('names.json', 'w') as file:
            json.dump(names, file)

    sendmsg(conn, "Здесь сегодня тесновато. Но для тебя всегда место найдется!")
    data = 'new'

    while data:
        data = checkmsg(conn)
        if data not in command:
            print(data)
        else:
            logging.info(f'Command {data}')
