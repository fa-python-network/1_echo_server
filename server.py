import socket

sock = socket.socket()
default_port = 9090
while True:
    try:
        port = int(input("Введите порт на котором хотите меня поднять: "))
        if port > 65535 or port < 0:
            print("Порт должен быть числом в диапазоне 0-65535")
        else:
            break
    except TypeError:
        print("Порт должен быть числом в диапазоне 0-65535")

try:
    sock.bind(('', port))
except ConnectionError:
    print("Похоже, к этому порту нельзя причалиться =( пробую стандартный . . .")
    try:
        sock.bind(('', default_port))
    except Exception:
        print("Случилось что-то сверхъестественное . . .")
        exit(-1)

sock.listen(0)


while True:
    conn, addr = sock.accept()
    print(addr)

    msg = ''

    while True:
        data = conn.recv(1024)
        if not data:
            break
        msg += data.decode()
        conn.send(data)

    print(msg)
    conn.close()
