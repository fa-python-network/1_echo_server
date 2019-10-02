import socket
import logging
import json
import hashlib
import secrets

logging.basicConfig(filename="sample.log", level=logging.INFO)

with open('sessions.json') as json_file:
    sessions_json = json.load(json_file)
    json_file.close()

with open('users.json') as json_file1:
    Users = json.load(json_file1)
    json_file1.close()


def get_port(port):
    if port == "":
        port = int(input('Введите порт от 1024 до 65535: \n'))
    else:
        port += 1
    if 1023 < port < 65535:
        return port
    logging.error('Не валидный порт')
    print('Не валидный порт')
    return get_port()


sock = socket.socket()

port = get_port("")

while True:
    try:
        sock.bind(('', port))
        break
    except BaseException:
        logging.error('Ошибка создания прослуштвания')
        print('Ошибка создания прослуштвания')
        port = get_port(port)

logging.info('Сервер запущен на порту: ' + str(port))
print('Сервер запущен на порту: ', port)

sock.listen(1)

while True:
    conn, addr = sock.accept()
    logging.info(addr)

    while True:
        user = conn.recv(1024)
        user = user.decode()
        user = json.loads(user)
        if user["comand"] == "1":
            print(user['User']['login'])
            h = hashlib.md5(user['User']['pass'].encode())
            pas = h.hexdigest()

            Users.append({
                "login": user['User']['login'],
                "pass": pas,
                "Name": user['User']['name']
            })

            with open('users.json', 'w') as json_file2:
                json.dump(Users, json_file2)
                json_file2.close()

            touk = secrets.token_hex(16)
            sessions_json[touk] = {"login": user['User']['login'], "Name": user['User']['name']}

            with open('sessions.json', 'w') as json_file2:
                json.dump(sessions_json, json_file2)
                json_file2.close()

            conn.send(json.dumps(
                {"tok": touk, "user": {"login": user['User']['login'], "Name": user['User']['name']}}).encode())
            break
        elif user["comand"] == "2":
            flag = 0
            for i in Users:
                if i['login'] == user['User']['login']:
                    h = hashlib.md5(user['User']['pass'].encode())
                    pas = h.hexdigest()
                    if i['pass'] == pas:
                        touk = secrets.token_hex(16)
                        sessions_json[touk] = {"login": i['login'], "Name": i['Name']}

                        with open('sessions.json', 'w') as json_file2:
                            json.dump(sessions_json, json_file2)
                            json_file2.close()

                        conn.send(json.dumps(
                            {"tok": touk, "user": {"login": i['login'], "Name": i['Name']}}).encode())
                        flag = 1
                    else:
                        conn.send(json.dumps(
                            {"tok": "", "user": {}}).encode())
            if flag == 1:
                break

        elif user["comand"] == "3":
            touk = user["tok"]
            sessions_json[touk]
            conn.send(json.dumps(sessions_json[touk]).encode())
            break

    msg = ''

    while True:
        data = conn.recv(1024)
        if not data:
            break
        msg += data.decode()
        conn.send(data)

    logging.info(msg)

    conn.close()
