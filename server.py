# -*- coding: utf-8 -*-
import socket
import csv

def ask_send(conn, ask):
    '''Функция отправки сообщения'''
    conn.send(ask.encode())
    
                    
                
    
    


    

sock = socket.socket()
f = open("log.txt", "w")

# Безопасно вводим номер порта
try:
    portnum = int(input("Select port number\n"))

except:
    portnum = 9090
    f.write("Wrong format of port number\n")

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

#######################################



while True:
# Запускает процесс прослушивания.

    # Реализация сервера идентификации
    sock.listen(1)
    f.write("Server is listening\n")

    conn, addr = sock.accept()
    print(addr, "connected")
    f.write("User " + str(addr) + " connected\n")

    known = False

    with open("list.csv", "r") as ls:

        for line in csv.reader(ls):
            if line[0] == addr[0]:
                ask_send(conn, "Welcome, " + line[1])
                known = True
                f.write("Known user connected\n")

        ls.close()
        
    if not known:
        ask_send(conn, "Who are you?")

        

        try:
            data = conn.recv(1024)
            name = data.decode()

            with open ("list.csv", "a") as inls:
                csv.writer(inls).writerow([addr[0], name])
                inls.close()

            f.write("User added as " + name + "\n")

        except:
            name = "Guest"
            ask_send(conn,"Wrong format of name. You are a guest.")

            with open ("list.csv", "a") as inls:
                csv.writer(inls).writerow([addr[0], name])
                inls.close()

            f.write("User added as Guest\n")

        ask_send(conn, "Welcome, " + name)


    while True:
    # Запись и вывод полученных сообщений.
        
        try:
            data = conn.recv(1024)
            msg = data.decode()
            if not data:
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


