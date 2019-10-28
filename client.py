import socket
print("Запуск")
from time import sleep

print("Установка соединения")
print("Введите IP")
sIP = input()
print("Введите порт")
Sport = input()

sock = socket.socket()
sock.setblocking(1)
sock.connect((sIP, Sport))

msg = " "
While (msg == "exit"): 
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
