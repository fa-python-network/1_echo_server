import socket
import json


def mem(ipv):
    with open('names.json', "a") as file:
        memory = json.load(file)
    if ipv not in memory:
        return False
    else:
        return True


sock = socket.socket()
port = 9090
try:
    sock.bind(('192.168.0.100', port))
except:
    port+=1
    sock.bind(('192.168.0.100', port))
sock.listen(4)
command = ("exit")
while True:
    conn, addr = sock.accept()
    print(addr)
    msg = 'Добрый вечер'
    conn.send(msg.encode())
    data = 'new'
    while data:
        data = conn.recv(1024)
        data = data.decode()
        if data not in command:
            print(data)
        else:
            with open("log_serv.json", "a") as file:
                json.dump(data, file)






