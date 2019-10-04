import socket
import logging
import csv
import sys
import base64

#Функция авторизации пользователей
def auth (addr):

    ip = addr[0]
    arr = {}

    #Чтение списка пользователей из csv файла
    with open('users.csv', 'r') as users:
        reader = csv.reader(users)
        for row in reader:
            for i in range(len(row)):
                cur_arr = row[i].split(";")
                arr[cur_arr[0]] = [cur_arr[1],cur_arr[2]]

    #Проверка пользователя, передача соответствующих сообщений 
    if str(ip) in arr.keys():
        conn.send(("Введите пароль: ").encode())
        password = conn.recv(1024).decode()
        if password == arr[str(ip)][1]:
            hi_msg = "Добро пожаловать, " + str(arr[str(ip)][0])
            conn.send(hi_msg.encode())

    else:
        reg(ip, arr)

#Функция регистрации пользователей        
def reg(ip, arr):

    conn.send(("Введите Ваше имя: ").encode())
    name = conn.recv(1024).decode()
    conn.send(("Придумайте пароль: ").encode())
    password = conn.recv(1024).decode()
    hi_msg = "Добро пожаловать, " + name 
    conn.send(hi_msg.encode())
    new_user = [str(ip), name, password]
    with open('users.csv', 'w', newline='') as users:
        writer = csv.writer(users, delimiter = ';')
        writer.writerow(new_user)

logger = logging.getLogger("logger")
logger.setLevel(logging.INFO)
log_handler = logging.FileHandler(filename = "info.log", encoding = "UTF-8")
log_handler.setLevel(logging.INFO)
logger.addHandler(log_handler)

stand_port = 9090
print("Введите номер порта: ")
inp_port = int(input())

if inp_port == 0:
    inp_port = stand_port
elif inp_port >=0 and inp_port <= 1024:
    print("Данный порт занят, введите новое значение: ")
    inp_port = int(input())

port = inp_port

sock = socket.socket()  

#Автоподбор свободного порта

con_res = False
while con_res == False:
    try:
        sock.bind(('', port))
        con_res = True
    except OSError:
        port = port+1

if port != inp_port:
    print("Порт: ", inp_port, "занят; Прослушивается порт: ", port)
else:
    print("Прослушивается порт: ", port)

sock.listen(1)

while True:

    conn, addr = sock.accept()
    logger.info(addr)

    #
    auth(addr)
            
    conn.send("Введите сообщение; Для выхода введите exit: ".encode())
    
    #Прием сообщений
    msg = ''

    while True:
        data = conn.recv(1024)
        if not data:
            break
        msg += data.decode()

    print(msg)

    conn.close()
      