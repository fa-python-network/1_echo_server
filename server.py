import socket
import json


def mem(ipv):
    with open('names.json', "r") as file:
        memory = json.load(file)
        if ipv not in memory:
            return False
        else:
            return memory[ipv]





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
    check = mem(addr[0])
    if check:
        msg = f'Добрый вечер, {check}!'
        conn.send(msg.encode())
    else:
        msg = "Введите, ваше имя:"
        conn.send(msg.encode())
        name = conn.recv(1024)
        name = name.decode()
        with open('names.json', 'r') as file:
            names = json.load(file)
            names[addr[0]] = name
        with open ('names.json', 'w') as file:
            json.dump(names, file)
        msg = "Здесь сегодня тесновато. Но для тебя всегда место найдется!"
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






