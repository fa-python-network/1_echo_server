# -*- coding: utf-8 -*-
import socket
import csv

def ask_send(conn, ask):
    '''Функция отправки сообщения. Принимает conn и само сообщение'''
    conn.send(ask.encode())

def msg_recv(conn):
    '''Функция принятия сообщения. Принимает conn.'''
    data = conn.recv(1024)
    return data.decode()
    

sock = socket.socket()
f = open("log.txt", "w")

# Безопасно вводим номер порта
while True:
    try:
        portnum = int(input("Write port number\n"))
        if 1024 <= portnum <= 65535:
            break
        else:
            print("Wrong format of port number")
            f.write("Wrong format of port number\n")

    except:
        print("Wrong format of port number, default set")
        portnum = 9090
        f.write("Wrong format of port number, default set\n")
        break

while True:
# Безопасно задаем номер порта. В случае ошибки, повышаем значение на единицу

    try:
        sock.bind(('', portnum))
        print("Using port:", portnum)
        f.write("Server runs\n")
        break

    except:
        portnum += 1
        f.write("Port number is changed\n")
        print("Using port:", portnum)

while True:
# Запускает процесс прослушивания.

    # Реализация сервера идентификации
    sock.listen(1)
    f.write("Server is listening\n")

    conn, addr = sock.accept()
    print(addr, "connected")
    f.write("User " + str(addr) + " connected\n")

    known = False
    
    # Чтение файла с именами
    with open("list.csv", "r") as ls:

        for line in csv.reader(ls):
            if line[0] == addr[0]:
                ask_send(conn, "Enter password")
                
                while True:
                    pswd = msg_recv(conn)

                    if line[2] == pswd:
                        ask_send(conn, "Welcome, " + line[1])
                        f.write("Successed pswd\n")
                        break
                    else:
                        ask_send(conn, "Wrong password")
                        f.write("Wrong psswd\n")
                
                known = True
                f.write("Known user connected\n")
                break
            

        ls.close()
    
    # Если клиент неизвестен    
    if not known:
        ask_send(conn, "Who are you?")

        try:
            name = msg_recv(conn)
            f.write("User added as " + name + "\n")
            ask_send(conn, "Choose password")
            pswd = msg.recv(conn)

        except:
            name = "Guest"
            ask_send(conn,"Wrong format of name. You are a guest.")
            f.write("User added as Guest\n")
            ask_send(conn, "Choose password")
            pswd = msg.recv(conn)

        with open ("list.csv", "a") as inls:
            csv.writer(inls).writerow([addr[0], name, pswd])
            inls.close()

            

        ask_send(conn, "Welcome, " + name)


    while True:
    # Запись и вывод полученных сообщений.
        
        try:
            msg = msg_recv(conn)
            if not msg:
                print("No message recieved")
                conn.close()
                break

            if msg == "exit":
                print("Client exits")
                f.write("Disconnection\n")
                conn.close()
                break

            print(msg)
            f.write("Message recieved " + msg + "\n")

        except:
            conn.close()
            break


