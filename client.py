# -*- coding: utf-8 -
import socket

def ask_send(ask):
    '''Функция отправки сообщения. Принимает само сообщение'''
    sock.send(ask.encode())


def msg_recv():
    '''Функция принятия сообщения.'''
    data = sock.recv(1024)
    return data.decode()

while True:

    try:
        portnum = int(input("Write port number\n"))
        if 1024 <= portnum <= 65535:
            break
        else:
            print("Wrong format of port number")

    except:
        print("Wrong format of port number")

while True:

    try:
        hostname = raw_input("Write host address\n")
        for i in hostname.split("."):
            if 255 < int(i) or int(i) < 0:
                print("Wrong format of hostname")
                break
        break

    except:
        print("Wrong format of hostname, set default")
        hostname = "localhost"
        break

sock = socket.socket()
sock.connect((hostname, portnum))

while True:

    data = msg_recv()
    print(data)

    if data == "Who are you?":
        name = raw_input()
        ask_send(name)
    
    if data == "Choose password":
        pswd = raw_input()
        if pswd != "":
            ask_send(pswd)

    if data == "Enter password" or data == "Wrong password":
        pswd = raw_input()
        ask_send(pswd)

    if "Welcome" in data:
        break

while True:

    msg = raw_input("Write <exit> to quit\n")

    if msg == "exit":
        ask_send(msg)
        break

    ask_send(msg)
    print("Message sent")

sock.close()


