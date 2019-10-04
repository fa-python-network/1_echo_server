import socket
import hashlib
import json
import logging
from sendcheck import *

SALT = 'memkekazaza'.encode("utf-8")  # соль для хеширования
varcom = ['mymsg', 'send', 'exit']  # Список доступных команд

logging.basicConfig(filename="log_serv", level=logging.INFO)  # Настройки логгинга (( Взято у умного соседа))


def mem(ipv):  # Функция проверки ip адреса в базе
    with open('names.json', "r") as file:
        memory = json.load(file)
        if ipv not in memory:
            return False
        else:
            return memory[ipv][0]


def autoriz(ipv, passw):  # Функция проверки пароля
    with open('names.json', "r") as file:
        memory = json.load(file)
        if memory[ipv][1] == hashpass(passw):
            return True
        else:
            return False


def hashpass(passw: str):  # Функция хеширования данных
    return hashlib.sha512(passw.encode("utf-8") + SALT).hexdigest()


def mymessage(name):  # Функция проверки сообщений пришедших пользователю
    with open(name + '.txt', 'r') as file:
        text = file.read()
    with open(name + '.txt', 'w') as file:
        file.write('your message: \n')
    return text


def mail(name, msg, user):  # Функция отправки сообщения в файл пользователя
    with open(name + '.txt', 'a') as file:
        file.write(f'{user} : \n')
        file.write(msg + '\n')


sock = socket.socket()
port = 9090
portmiss = True
adress = ['localhost', '192.168.0.101']

while portmiss:  # Обработка подключения к порту
    try:
        sock.bind((adress[0], port))
        portmiss = False
    except:
        port += 1
sock.listen(4)
command = ("exit") # Команды для логгинга

while True:
    conn, addr = sock.accept()
    logging.info(f"Connect - {addr}")

    check = mem(addr[0])
    access = False
    if check:  # Ветка знакомого пользователя
        msg = f'Добрый вечер, {check}! Ваш пароль?'
        while not access:
            sendmsg(conn, msg)
            passw = checkmsg(conn)
            access = autoriz(addr[0], passw)
            msg = 'Неверный ввод!'
        sendmsg(conn, 'ДАРОВА')

    else:  # Ветка нового пользователя
        sendmsg(conn, "Введите, ваше имя и пароль:")
        name = checkmsg(conn)
        passw = checkmsg(conn)

        with open('names.json', 'r') as file:  # Сохранение пароля
            names = json.load(file)
            names[addr[0]] = [name, hashpass(passw)]
        with open('names.json', 'w') as file:
            json.dump(names, file)
        with open(name + '.txt', 'w') as file:  # Создание файла пользователя
            file.write('your message: \n')
    users = []
    with open('names.json', 'r') as file:  # Создание списка существующих юзеров и переменной активного юзера
        names = json.load(file)
        user = names[addr[0]][0]
        for name in names.values():
            users.append(name[0])

    sendmsg(conn, "Здесь сегодня тесновато. Но для тебя всегда место найдется!")
    data = True
    sendmsg(conn, f'Список доступных команд:{varcom}')

    while data:  # main цикл обрабатывает команды клиента
        data = checkmsg(conn)
        if data == varcom[0]:
            sendmsg(conn, mymessage(user))
        elif data == varcom[1]:
            name = checkmsg(conn)
            if name in users:
                sendmsg(conn, 'Ваше письмо:')
                mail(name, checkmsg(conn), user)
                sendmsg(conn, 'Успешно!')
            else:
                sendmsg(conn, 'Нет такого пользователя!')
                sendmsg(conn, 'Попробуйте другое имя.')
        elif data in command:
            sendmsg(conn, 'Прощай!')
            logging.info(f'Command {data}')
        else:
            sendmsg(conn, 'Такой команды нету!')
