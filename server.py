import socket
import json


sock = socket.socket()
try:
    num_port = int(input("Введите номер порта:"))
    assert 1024 < num_port < 65535, "Введенный порт рекомендуется не использовать или он занят."

except (AssertionError, TypeError, ValueError) as e:
    num_port = 9091

while True:
    try:
        sock.bind(('', num_port))
        break
    except OSError:
        num_port += 1

print("Слушает порт", " ", num_port)
print("Ожидайте подключения...")
sock.listen(1)
file = open("log.txt", "a")

while True:
    try:

        file.write("Подключение удачно \nИспользуется порт {}\t".format(num_port))
    except ValueError:
        file = open("log.txt", "a")
        file.write("Подключение удачно \nИспользуется порт {}".format(num_port))

    conn, addr = sock.accept()

    file.write("Адрес хоста: {}\n".format(addr))

    with open("login.json", "r") as log:
        data_login = json.load(log)
    if data_login.get(addr[0]):
        conn.send(f"Здравствуй, {data_login[addr[0]]}".encode())
    else:
        conn.send("Пожалуйста, введите ваше имя".encode())
        nam = conn.recv(1024).decode()
        data_login[addr[0]] = nam
        conn.send(f"Здравствуй, {data_login[addr[0]]}".encode())
    print(data_login)
    with open("login.json", "w") as log:
        json.dump(data_login, log)
    msg = ''

    while True:
        data = conn.recv(1024)
        if not data:
            break
        msg += data.decode()
        if data.decode() == "exit":
            file.write("Соединение разорвано!")
            file.close()
        conn.send(data.decode().upper().encode())

conn.close()
