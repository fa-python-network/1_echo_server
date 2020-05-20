# coding=utf-8
import socket
import logging


logging.basicConfig(filename="client.log", format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Клиент запущен')

def con(ip, sock, Name):
    sock.setblocking(1)
    sock.connect(ip)
    sock.send(Name.encode())


def recon(ip, sock):
    sock.setblocking(1)
    sock.connect(ip)


def msg_send(sock, l, msg, key):
    recon(l, sock)
    crypt = ''
    for i in msg:  #
        crypt += chr(ord(i) ^ key)
    msg = crypt
    sock.send(msg.encode())



def ip():
    while True:
        msg = input('IP сервера (пустая строка = localhost): ')
        if msg == "":  # default
            ip = '127.0.0.1'
            print('IP сервера ' + ip)
        else:
            ip = msg
            print('IP сервера ' + ip)
        break
    logging.info('Установлен ip адресс сервера '+ip)
    return ip


def port():
    while True:
        msg = input('Порт (пустая строка = 9090): ')
        if msg == "":  # default
            port = 9090
            print('Порт 9090')
        else:
            port = int(msg)
            print ('Порт ' + str(port))
        break
    return port


sock = socket.socket()
adr = ip()
P = port()
logging.info('Установлен порт '+str(P))
l = (adr, P)

while True:
    try:
        k = int(input('Введите ключ шифрования '))
        logging.info('Введен ключ шифрования')
        break
    except:
        logging.error("Введен неверный ключ")
        print('Введите любое число, главное чтобы оно совпадало на сервере и клиенте')


Name = 'name(' + str(input('Введите свое имя: ')) + ')'
msg_send(sock, l, Name, k)


print ('\n Для выхода из чата напишите exit \n')

while True:
    sock = socket.socket()

    msg = input('Введите сообщение: ')
    if msg != 'exit':
        logging.info('Отправленно сообщение ' + msg)
        msg_send(sock, l, msg, k)
    else:
        print ('Всего хорошего!')
        logging.info('Клиент завершил работу')
        break
    sock.close()
logging.info('Клиент остановлен')
