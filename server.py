import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(0)
with open ('log.txt', 'a') as file:
    file.write("Сервер запущен")

with open ('log.txt', 'a') as file:
    file.write("Начало прослушивания")
conn, addr = sock.accept()
with open ('log.txt', 'a') as file:
    file.write("Подключение клиента")

while True:
     data = conn.recv(1024)
     with open ('log.txt', 'a') as file:
         file.write("Получение данных от клинета")
     if not data:
         break
     conn.send(data.upper())
with open ('log.txt', 'a') as file:
    file.writeln("Клиент отключился")     
