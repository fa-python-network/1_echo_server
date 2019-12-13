import socket
import json
import logging as l


log_format = '%(levelname)s %(asctime)s - %(message)s'
l.basicConfig(filename='server.log', format = log_format ,datefmt='%d.%m.%Y %H:%M:%S', level=l.INFO)
l.info('Start logging INFO')

port = 9090
sock = socket.socket()


def check(host_name):
    with open('user.json', "r") as file:
        user_d = json.load(file)
        if host_name in user_d:
            return user_d[host_name]
        else:
            return False


while True:
    try:
        sock.bind(('', port))
        break
    except:
        l.info(f'Port {port} is busy')
        port += 1
        
l.info (f'Server connected to port: {port}')
print (f'Server connected to port: {port}')
sock.listen(0)
l.info('Server waits for connection...')



while True:
    conn, addr = sock.accept()
    l.info(f'Client {addr} connected to server')

    ch = check(addr[0])
    if ch:
        msg = f'Hello, {ch}!'
        conn.send(msg.encode())
    else:
        msg = 'Please, write your name:'
        conn.send(msg.encode())
        name = conn.recv(1024)
        name = name.decode()
        with open('user.json', 'r') as file:
            users = json.load(file)
            users[addr[0]] = name                  
        with open ('user.json', 'w') as file:
            json.dump(users, file)
            msg = f"Hello, {name}"
            conn.send(msg.encode())

    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.send(data)
        l.info ('Server sent an answer')        

    conn.close()
    l.info('Connection is closed')