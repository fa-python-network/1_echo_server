# coding=utf-8
import socket
import logging

logging.basicConfig(filename="server.log", format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Сервер запущен')

def port(sock):
    global port
    while True:
        try:
            msg = input('Порт (пустая строка = 9090)')
            if msg == "":  # default
                port = 9090
                sock.bind(('', port))
                break
            else:
                port = int(msg)
                sock.bind(('', port))
                break
        except:
            logging.error("Порт "+int(port)+" занят")
            print('Порт занят')
            por = port +1
            port = int(por)
            break
    return port


while True:
    try:
        key = int(input('Введите ключ шифрования '))
        logging.info('Введен ключ шифрования')
        break
    except:
        print('Введите любое число, главное чтобы оно совпадало на сервере и клиенте')
        logging.error("Неверные символы ключа шифрования")

def message(conn, key):
    msg = conn.recv(1024).decode()
    crypt = ''
    for i in msg:
        crypt += chr(ord(i) ^ key)
    return crypt


def login(addr, text,c,e):
    global name
    f = open('login_info.txt', 'a')
    fr = open('login_info.txt', 'r')
    a = sum(1 for line in open('login_info.txt', 'r'))
    b = 0
    if text[:4] == 'name':
        for line in fr.readlines():
            b += 1
            li = line.partition(':')[2]
            if li[:-1] == addr[0]:
                name = line.partition(':')[0]
                N = str(name)[1:-1]
                if c==0:
                    print ('Приветствуем вас, ' + N)
                    logging.info('Залогинился пользователь '+name+addr[0])
                    c=1
                    break
            if b == a and li[:-1] != addr[0]:
                name = text[4:]
                N = str(name)[1:-1]
                f.write(name + ':' + str(addr[0]) + '\n')
                if e==0:
                    print ('Привет,' + N + '! Вы тут первый раз? Теперь вы зарегестрированны')
                    logging.info('Зарегистрирован новый пользователь ' + name + addr[0])
                    e=1
                    break

    f.close()
    fr.close()
    return name


sock = socket.socket()
P = port(sock)
print ('Успешное подключение к порту ' + str(P))
logging.info('Успешное подключение к порту ' + str(P))
c=0
e=0
while True:
    sock.listen(1)
    conn, addr = sock.accept()
    text = message(conn, key)
    name = login(addr, str(text),c,e)
    logging.info('Получено сообщение '+name+text)
    print(name, text)
    conn.close()


logging.info('Сервер остановлен')