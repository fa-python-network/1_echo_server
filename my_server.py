import socket


#настройки
port = 9100
maxclients = 1

print('Python Socket Server ver. 0.0.1. By Igor Stepanov (PI18-2)');
sock = socket.socket()  #общая часть для клиента и сервера

sock.bind(('',port))    #занимаем 9100 порт
print(f'Занял порт {port}')
sock.listen(maxclients) #начинаем слушать, ожидать единственное подключение
print(f'Начал слушать порт {port}')
print('Ожидаю подключений...')

conn, addr = sock.accept()  #принимаем от клиента сокет и его адрес

while True:
    print(f'В данный момент получаю данные от клиента {addr}')
    data = conn.recv(1024)  #принимаем по 1 КБ
    if not data:
        break
    conn.send(data) #возвращаем клиенту его же данные
    print(f'Отправляю ответ клиенту {addr}')
    
conn.close()    #закрыть соединение с клиентом
print('Соединение закрыто')