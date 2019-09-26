import socket


#настройки
port = 9100
maxclients = 1

log_file = open('server.log','a')  #лог файл

log_file.write(f'Python Socket Server ver. 0.0.1. By Igor Stepanov (PI18-2)\n');
sock = socket.socket()  #общая часть для клиента и сервера

sock.bind(('',port))    #занимаем 9100 порт
log_file.write(f'Занял порт {port}\n')
sock.listen(maxclients) #начинаем слушать, ожидать единственное подключение
log_file.write(f'Начал слушать порт {port}\n')
log_file.write(f'Ожидаю подключений...\n')

while True:     #сервер, не спи, всегда внимательно слушай!

    conn, addr = sock.accept()  #принимаем от клиента сокет и его адрес

    while True:
        log_file.close()
        log_file = open('server.log','a')  #лог файл
        log_file.write(f'В данный момент получаю данные от клиента {addr}\n')
        data = conn.recv(1024)  #принимаем по 1 КБ
        if not data:
            break
        conn.send(data) #возвращаем клиенту его же данные
        log_file.write(f'Отправляю ответ клиенту {addr}\n')
        
    conn.close()    #закрыть соединение с клиентом
    log_file.write(f'Соединение закрыто\n')
    log_file.close()