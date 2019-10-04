import socket
import re
from sendcheck import *


def acceptadr(adr):  # Функция проверки адреса через регулярные выражения
    if re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', adr) is None:
        return False
    if re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', adr).group(0) == adr:
        return adr


def acceptport(port):  # Функция проверки порта через регулярные выражения
    if re.match(r'\d{1,4}', port) is None:
        return False
    if re.match(r'\d{1,4}', port).group(0) == port:
        return port


adressation = ['localhost', '192.168.0.101']  # Список возможных адресов по умолчанию

go = True  # Переменные проверки адреса и порта
po = True
while go or po:
    print("Введите адрес хоста: ((Пустая строка ввод по умолчанию))")
    adress = input()
    print("Введите порт: ")
    port = input()
    if acceptadr(adress):
        go = False
    if acceptport(port):
        po = False
    if adress == "" or adress == 'localhost':
        adress = adressation[0]
        go = False
    if port == '':
        port = '9090'
        po = False

port = int(port)
sock = socket.socket()
sock.connect((adress, port))  # Подключение к серверу
ans = checkmsg(sock)
print(ans)
access = False

if "Введите" in ans:  # Ветка создания нового пользователя
    name = input()
    sendmsg(sock, name)
    passw = input()
    sendmsg(sock, passw)
else:
    while not access:  # Ветка проверки пароля
        passw = input()
        sendmsg(sock, passw)
        ans = checkmsg(sock)
        print(ans)
        if ans == 'ДАРОВА':
            access = True

print(checkmsg(sock))
print(checkmsg(sock))
ex = True
while ex:  # Main цикл, позволяет отправлять и читать сообщения от других пользователей.
    msg = input()
    if msg == "exit":
        ex = False
    sendmsg(sock, msg)
    if msg == 'send':
        sendmsg(sock, input())
        ans = checkmsg(sock)
        print(ans)
        if 'письмо' in ans:
            sendmsg(sock, input())
    print(checkmsg(sock))
sock.close()
