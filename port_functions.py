import socket
import hashlib
import getpass

def check_port(port, default=9090, lower_bound=1024,upper_bound=65536):
    """ Проверяет порт на соответствие диапазону и при несоответствии назначает порт по умолчанию."""
    port=int(port)
    if lower_bound<port<upper_bound:
        pass
    else:
        port=default
    return port

def check_host(host):
    """Проверяет хост: либо localhost, либо IP-адрес."""
    if host=='localhost':
        return host
    else:
        valid=True
        l=host.split('.')
        if len(l)==4:
            for n in l:
                if 0<=int(n)<=255:
                    pass
                else:
                    valid=False
                    break
        else:
            valid=False
    if not(valid):
        host='localhost'
    return host

def change_port(port,server_socket):
    """Проверка, занят ли порт с этим сокетом. При занятости порта происходит его инкремент."""
    while(True):
        try:
            server_socket.bind(('',port))
        except socket.error:
            port+=1
        else:
            print("{} - номер порта".format(port))
            break

def check_user(ip,file="users.txt"):
    """Проверка наличия пользователя в системе по данному IP-адресу"""
    log_in_successful=bool() 
    try:
        user_list=create_user_list(file) 
    except IOError as e: # если не удалось прочитать из файла, вывести сообщение об ошибке и создать его
        print("Данного файла не существует!")
        f=open(file,"w")
        f.close()
        log_in_successful=False
    else:
        user_exists=False
        for user in user_list: 
            if ip==user[1]: # если пользователь существует, спросить пароль и попробовать залогиниться
                entered_password=getpass.getpass("Введите пароль: ")
                log_in_successful=log_in_user(user, entered_password)
                user_exists=True
                break
        if not(user_exists): # если пользователя не существует, добавить
            name=input("Введите имя пользователя: ")
            password=getpass.getpass("Введите пароль: ")
            add_user(ip,name, password, file)
            log_in_successful=False
    return log_in_successful
    
def add_user(ip,name,password,file="users.txt"):
    """Добавить пользователя с данным именем и IP-адресом"""
    users_file=open(file,"a") #открывает файл на дозапись
    name.strip()
    password.strip() #удаляет лишние пробелы
    users_file.write("{};{};{}\n".format(name,ip,encode(password)))
    print("Пользователь {} добавлен в систему".format(name))
    users_file.close()
    
def create_user_list(file="users.txt"):
    """Создаёт список с именами и ip-адресами пользователей"""
    users_file=open(file,"r")
    user_list=list()
    for line in users_file: #читает записи из файла, разделяя поля по ; и добавляя в список
        user=line.split(";")
        user_list.append(user)
    return user_list
    users_file.close()
            
def log_in_user(user,entered_password):
    """Вход пользователя с паролем"""
    if(encode(entered_password)==user[2].strip()): #шифрование пароля и сравнение с паролем из файла
        print("Пользователь {} вошёл в систему".format(user[0]))
        return True
    else:
        print("Неверный пароль!")
        return False

def encode(password):
    """Безопасное хранение паролей"""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def send_message(sock,message,header_length=10):
    """Отправить сообщение в сокет, добавляя заголовок заданной длины """
    message_length=len(message)
    header="0"*(header_length-len(str(message_length)))+str(message_length)
    message=header+message
    sock.send(message.encode())

def receive_message(sock,header_length=10):
    message=''
    conn,address=sock.accept()
    header=conn.recv(header_length).decode()
    try:
        message_length=int(header.lstrip("0"))
    except ValueError as e:
        pass
    else:
        print(message_length)
        message=conn.recv(message_length).decode()
        print(message)
    finally:
        conn.close()
