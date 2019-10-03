import json
import socket
from myserver import Myserver
f = open ('log.txt', 'w')
sock = Myserver()
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
    conn, addr = sock.newclient()
    print(f"{addr[0]}")
    print("connection: " + f"{addr}", file = f)
    with open("dataClients.json", "r+") as d:    #проверка пользователя с помощью файла
        data = json.loads(d.read())
        for i in data['clients']: #цикл на проверку пользователя
            if i['ip'] == addr[0]:
                conn.sendmessage('Hello, enter the password: ')
                if conn.newmessage() != i['password']:
                    conn.sendmessage('It\'s Not Correct')
                    conn.close()
                    cor = False
                else:
                    conn.sendmessage((f'Hello {i["name"]}'))
                    cor = True
                break
        else: #добавление нового
            conn.sendmessage('Hello, You\'re new, please enter you name ')
            name = conn.newmessage()
            conn.sendmessage('And you\'re secret password ')
            password= conn.newmessage()
            newclient = {"ip": addr[0], "name": name, "password": password}
            data['clients'].append(newclient)
            d.seek(0)
            d.write(json.dumps(data))
            d.truncate()
            conn.sendmessage('congratulation')
            cor = True

    msg = ''
    e = ''
    data = ''
    while cor:

        data = conn.newmessage()
        print("new data from cliqent", file = f)
        if not data:
            break
        msg += data
        conn.sendmessage(data)
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


