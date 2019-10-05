import socket, errno
import sys

def close_server():
	with open ('log.txt', 'a') as file:
		print('Остановка сервера', file=file)
	global sock
	sock.close()
	sys.exit()

def new_user(conn, addr, d):
    name = conn.recv(1024).decode()
    conn.send('1'.encode())
    password = conn.recv(1024).decode()
    d[addr[0]] = d.get(addr[0], [name, password])
    with open ('users.txt', 'w') as users:
        print(d, file=users)


def old_user(conn, addr, d):
    passwd = d[addr[0]][1]
    password = conn.recv(1024).decode()
    if passwd == password:
        conn.send(str(0).encode())
        conn.recv(1024)
        return
    else:
        conn.send(str(1).encode())
        old_user(conn, addr, d)
    
        


def main():
    global sock

    #Поиск свободного порта
    port = 9090
    flag = 1
    while flag:
        try:
            sock.bind(('', port))
        except socket.error as e:
            if e.errno == errno.EADDRINUSE:
                port+=1
        else:
            flag = 0
    print(port)


    #Считывание всех зареганых клиентов
    try:
        with open ('users.txt', 'r') as users:
            d = eval(users.read())
    except FileNotFoundError:
        with open ('users.txt', 'w') as users:
            d={}
    except SyntaxError:    
            d={}



    with open ('log.txt', 'a') as file:
		    print('Запуск сервера', file=file)
    sock.listen(1)

    with open ('log.txt', 'a') as file:
	    print('Начало прослушивания порта', file=file)


    while True:


        conn, addr = sock.accept()
        with open ('log.txt', 'a') as file:
            print('Подключение клиента', file=file)		
        
    #Считывание имени клиеента и пароля
        if addr[0] not in d.keys():
            flag = str(1)
            conn.send(flag.encode())
            new_user(conn, addr, d)
        else:
            flag = str(0)
            conn.send(flag.encode())
            old_user(conn, addr, d) 

        msg = 'Hello ' + d[addr[0]][0]
        conn.send(msg.encode())
        
        while True:
            data = conn.recv(1024).decode()
            with open ('log.txt', 'a') as file:
                print('Приём данных от клиента', file=file)
            if not data:
                conn.close()
                break
            
            conn.send(data.upper().encode())
            with open ('log.txt', 'a') as file:
                print('Отправка данных клиенту', file=file)


        with open ('log.txt', 'a') as file:
            print('Отключение клиента', file=file)



sock = socket.socket()
try:
    main()
except KeyboardInterrupt:
    close_server()



















