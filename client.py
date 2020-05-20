import socket

sock = socket.socket()

while True:
    try:
        address = input("Введите адрес сервера: ")
        if address == '':
            address = 'localhost'
        while True:
            port = int(input("Укажите порт (диапозон 1024-65535): "))
            if 1024 <= port <= 65535:
                break
        sock.connect((address, port))
    except (socket.error, ValueError):
        print("Повторите ввод!")
    else:
        break

# массив для имитации трёх сообщений от пользователя
msg = ["na sozvone", "metnulsa kabanchikom","xochy kyrochky", "exit"]

# Цикл для имитации ввода сообщений пользователем
for i in range(len(msg)):
    sock.send(msg[i].encode())
    data = sock.recv(1024)
    print(data.decode())

sock.close()
