import socket

sock = socket.socket()

port=8080
sock.connect(('localhost', port))
print(f'Клиент подлкючился к серверу {port}')

print('Введите текст сообщения')
data = input()

print('Отправка сообщения')
sock.send(data.encode())

ans=sock.recv(1024) #ответ от сервера

sock.close()

print(ans.decode()) # вывод ответа в консоль

