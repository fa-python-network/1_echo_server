import socket
import re
import json


def checker():
    port = "4000"
    host = "localhost"
    print("default host is 127.0.0.1(localhost)\n"
          "default port is 4000"
          )
    while True:
        uhost = input("vvedite host:\n")
        if uhost == "default" or uhost == "localhost" or uhost == "lh":
            break
        elif re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', uhost) == None:
            print("try again")
        else:
            host = uhost
            break
    while True:
        uport = input("vvedite port:\n")
        if uport == "default" or uport == "4000":
            break
        elif not uport.isnumeric() == True or int(uport)<1024 or int(uport) > 65535:
            print("try again")
        else:
            port = uport
            break
    return host, int(port)

res = checker()

sock = socket.socket()
sock.setblocking(1)
sock.connect(res)
msg = ""

try:
    users_source = open("users_list.json", "r")
    usrs = users_source.read()
    users_current = json.loads(usrs)
    users_source.close()
except:
    pass



try:
    server_answer = sock.recv(1024).decode()
    print(server_answer)
except:
    print("reading error")

if "hi" not in server_answer:
    msg = input("login:\n")
    sock.send(msg.encode())


print('TYPE YOUR MESSAGES HERE, "exit" TO DISCONNECT')
while True:
    msg = input()
    # msg = "Hi!"
    sock.send(msg.encode())
    if "exit" in msg:
        print("DISCONNECTING...")
        break

sock.close()
