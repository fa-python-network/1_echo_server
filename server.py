import socket

sock = socket.socket()
sock.bind(('', 9092))
print('Запуск сервера')
print('Начало прослушивания порта')
sock.listen(1)
cm =''

while cm != 'stop':
    sock.listen(1)
    conn, addr = sock.accept()

    print ('connected:', addr)

    
    print('Прием данных от клиента')
    while True:
        data = conn.recv(1024)
        msg=''
        if not data:
            break
        msg+=data.decode()
        
        conn.send(data.upper())
        print(msg)
    print('Введи stop для отключения сервера')
    cm = input()
    print('Отправка данных клиенту')
    print('Отключение клиента')

conn.close()