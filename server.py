import json
import socket
f = open ('log.txt', 'w')
sock = socket.socket()
freeHost = 1025
while True:
    try:
        if freeHost == 65536:
            print('All ports busy')
            break
        sock.bind(('', freeHost))
        break
    except:
        freeHost += 1
print(freeHost)
print("Server starts", file = f)
print("Server starts")
sock.listen(0)
print("Now listen", file = f)

while True:
    conn, addr = sock.accept()
    print(f"{addr[0]}")
    print("connection: " + f"{addr}", file = f)
    with open("dataClients.json", "r+") as d:
        data = json.loads(d.read())
        for i in data: #цикл на проверку пользователя
            if i['ip'] == addr[0]:
                conn.send(b'Hello, enter the password: ')
                if (conn.recv(1024)).decode() != i['password']:
                    conn.send(b'It\'s Not Correct')
                    conn.close()
                    cor = False
                else:
                    conn.send((f'Hello {i["name"]}').encode())
                    cor = True
                break
        else: #добавление нового
            conn.send(b'Hello, You\'re new, please enter you name ')
            name = conn.recv(1024).decode()
            conn.send(b'And you\'re secret password ')
            password= conn.recv(1024).decode()
            newclient = {"ip": addr[0], "name": name, "password": password}
            data.append(newclient)
            d.seek(0)
            d.write(json.dumps(data))
            d.truncate()
            conn.send(b'congratulation')
            cor = True
   #проверка пользователя с помощью файла
    msg = ''
    e = ''

    while cor:

        data = conn.recv(1024)
        print("new data from cliqent", file = f)
        if not data:
            break
        msg += data.decode()
        conn.send(data)
        print("data to client", file = f)


    print(msg)

    conn.close()
    print('stop client', file = f)
    e = input('To stop vvevide \'stop\' if not something else: ')
    if e == 'stop':
        sock.close()
        print('server stop', file = f)
        f.close()
        break


