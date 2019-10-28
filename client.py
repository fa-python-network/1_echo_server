import socket
print("Запуск")
from time import sleep

print("Установка соединения")
sock = socket.socket()
sock.setblocking(1)
sock.connect(('10.38.165.12', 9089))

print("Получения данных с консоли и отправка данных")
msg = input()
sock.send(msg.encode())

print("Прием данных от сервера")
data = sock.recv(1024)

print("закрытие")
sock.close()
print("Вывод данных и закрытие соединения")
print(data.decode())
print("Завершение программы")
