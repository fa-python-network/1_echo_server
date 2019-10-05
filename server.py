# -*- coding: utf-8 -*-
import socket

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



while True:
# Запускает процесс прослушивания.

    sock.listen(1)
    f.write("Server is listening\n")

    conn, addr = sock.accept()
    print(addr, "connected")
    f.write("User " + str(addr) + " connected\n")

    while True:
    # Запись и вывод полученных сообщений.
        
        try:
            data = conn.recv(1024)
            msg = data.decode()
            if not data:
                print("No message recieved")
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


