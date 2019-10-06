import socket
import json
from hashlib import md5

ENCODING = 'utf-8'


def identify(conn: socket.socket, addr: tuple) -> None:
    """
    Функция идентификации
    """
    with open("login.json", "r") as log:
        data_login = json.load(log)
    if data_login.get(addr[0]):
        conn.my_send(f"Здравствуй, {data_login[addr[0]]}")
    else:
        conn.my_send("Пожалуйста, введите ваше имя")
        nam = conn.my_recv()
        data_login[addr[0]] = nam
        conn.my_send(f"Здравствуй, {data_login[addr[0]]}")
    print(data_login)
    with open("login.json", "w") as log:
        json.dump(data_login, log)



def auth(conn: socket.socket) -> bool:
    """
    Функция аутентификации
    """
    with open("auth.json", "r") as auth:
        data_auth = json.load(auth)
    conn.my_send("Введите ваше имя")
    name = conn.my_recv()
    conn.my_send("Введите ваш пароль")
    pas = conn.my_recv()
    h_pas = md5(pas.encode(ENCODING)).hexdigest()
    if name in data_auth and data_auth[name] == h_pas:
        conn.my_send("Здравствуй, {}, ты прошел аутентификацию(мои врата). Молодец!".format(name))
        return True
    else:
        conn.my_send("Мой дорогой {}, ты не прошел! Мы с тобой не знакомы.".format(name))
        return False


def my_send(self: socket.socket, msg: str) -> None:
    """
    Метод отправки сообщения с заголовком фиксированной длины
    """
    head = len(msg)
    fm = f'{head:4}{msg}'
    self.send(fm.encode(ENCODING))

def my_recv(self: socket.socket) -> str:
    """
    Метод получения текстового сообщения с фиксированным заголовком
    """
    head = int(self.recv(4).decode(ENCODING))
    msg = self.recv(head*2).decode(ENCODING)
    return msg

socket.socket.my_send = my_send
socket.socket.my_recv = my_recv




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

    # identify(conn,addr)
    auth_ = auth(conn)
    if not auth_:
        conn.close()
        continue
    msg = ''

    while True:
        data = conn.my_recv()
        if not data:
            break
        msg += data
        if data == "exit":
            file.write("Соединение разорвано!")
            file.close()
        conn.my_send(data.upper())

conn.close()
