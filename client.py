import socket
import re
from time import sleep

ENCODING = 'utf-8'


def my_send(self: socket.socket, msg: str) -> None:
    """
    Метод отправки сообщения с заголовком фиксированной длины
    """
    head = len(msg)
    self.send(f'{head:4}{msg}'.encode(ENCODING))


def my_recv(self: socket.socket) -> str:
    """
    Метод получения текстового сообщения с фиксированным заголовком
    """
    head = int(self.recv(4).decode(ENCODING))
    msg = self.recv(head*2)
    return msg.decode(ENCODING)


socket.socket.my_send = my_send
socket.socket.my_recv = my_recv

sock = socket.socket()

try:
    name_port = input("Введите имя хоста: ")
    assert re.match(r'[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}',
                    name_port) or name_port == "localhost", "Имя порта не котируется."
except (AssertionError, TypeError, ValueError) as e:
    print("Имя порта по умолчанию localhost")
    name_port = "localhost"

try:
    num_port = int(input("Введите номер порта: "))
    assert 1024 < num_port < 65535, "Введенный порт рекомендуется не использовать или он занят."
except (AssertionError, TypeError, ValueError) as e:
    print("Будет введен порт по умолчанию 9091")
    num_port = 9091

sock.connect((name_port, num_port))
print("Успешно!")
msg = ""
inf = sock.my_recv()
print(inf)
while msg != "exit" and "Мы с тобой не знакомы" not in inf:
    msg = input()
    sock.my_send(msg)

    inf = sock.my_recv()
    print(inf)

sock.close()
