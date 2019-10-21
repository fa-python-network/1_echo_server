import socket
import hashlib

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
    except IOError as e:
        print("Данного файла не существует!")
        f=open(file,"w")
        f.close()
        log_in_successful=False
    else:
        user_exists=False
        for user in user_list:
            if ip==user[1]:
                entered_password=input("Введите пароль: ")
                log_in_successful=log_in_user(user, entered_password)
                user_exists=True
                break
        if not(user_exists):
            name=input("Введите имя пользователя: ")
            password=input("Введите пароль: ")
            add_user(ip,name, password, file)
            log_in_successful=False
    return log_in_successful
    
def add_user(ip,name,password,file="users.txt"):
    """Добавить пользователя с данным именем и IP-адресом"""
    users_file=open(file,"a") 
    name.strip()
    password.strip()
    users_file.write("{};{};{}\n".format(name,ip,encode(password)))
    print("Пользователь {} добавлен в систему".format(name))
    users_file.close()
    
def create_user_list(file="users.txt"):
    """Создаёт список с именами и ip-адресами пользователей"""
    users_file=open(file,"r")
    user_list=list()
    for line in users_file:
        user=line.split(";")
        user_list.append(user)
    return user_list
    users_file.close()
            
def log_in_user(user,entered_password):
    if(encode(entered_password)==user[2].strip()):
        print("Пользователь {} вошёл в систему".format(user[0]))
        return True
    else:
        print("Неверный пароль!")
        return False

def encode(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()
