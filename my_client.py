import socket
from time import sleep

while True:
      host_name = input('Введите имя хоста:(например localhost) ')
      if host_name == 'localhost':
      		break
      else:
	        print('Ошибка')
while True:
      port = int(input('Введите порт: '))
      if 1024 <= port <= 65525:
         break
      else:
         print('Неправильный порт ')
sock=socket.socket()
sock.setblocking(1)
print(f'Идет подключение к хосту {host_name} и порту {port} ')
print('Идет подлючение к порту..')
sock.connect((host_name,port)) #Подключаемся к порту

#msg=input()
#msg="Hello, server!"
while True:
      msg = input('Для окончания работы с сервером введите exit ')
      if msg == "exit":
              sock.close()
              break
      sock.send(msg.encode())

data = sock.recv(1024)
sock.close()
print(data.decode())


