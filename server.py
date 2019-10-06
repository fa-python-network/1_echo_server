import socket, errno
import sys


def send_msg(msg, sock):
    length_msg = str(len(msg))
    length_msg = '0'*(10-len(length_msg)) + length_msg
    msg = length_msg + msg
    sock.send(msg.encode())

def recv_msg(sock):
    length_msg = int(sock.recv(10).decode())
    msg = sock.recv(length_msg).decode()
    return msg


def close_server():
	with open ('log.txt', 'a') as file:
		print('Остановка сервера', file=file)
	global sock
	sock.close()
	sys.exit()

def new_user(conn, addr, d):
    name = recv_msg(conn)
    send_msg('1', conn)
    password = recv_msg(conn)
    d[addr[0]] = d.get(addr[0], [name, password])
    with open ('users.txt', 'w') as users:
        print(d, file=users)


def old_user(conn, addr, d):
    passwd = d[addr[0]][1]
    password = recv_msg(conn)
    if passwd == password:
        send_msg('0', conn)
        recv_msg(conn)
        return
    else:
        send_msg('1', conn)
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
            send_msg(flag, conn)
            new_user(conn, addr, d)
        else:
            flag = str(0)
            send_msg(flag, conn)
            old_user(conn, addr, d) 

        msg = 'Hello ' + d[addr[0]][0]
        send_msg(msg, conn)
        
        while True:
            data = recv_msg(conn)
            with open ('log.txt', 'a') as file:
                print('Приём данных от клиента', file=file)
            if not data:
                conn.close()
                break
            
            send_msg(data.upper(), conn)
            with open ('log.txt', 'a') as file:
                print('Отправка данных клиенту', file=file)


        with open ('log.txt', 'a') as file:
            print('Отключение клиента', file=file)



sock = socket.socket()
try:
    main()
except KeyboardInterrupt:
    close_server()



















