import socket

def check_port(port, default):
    """ Проверяет порт на соответствие диапазону и при несоответствии назначает порт по умолчанию."""
    port=int(port)
    if 1024<port<65536:
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
    try:
        user_list=create_user_list(file)
    except IOError as e:
        print("Данного файла не существует!")
        f=open(file,"w")
        f.close()
    else:
        user_exists=False
        for user in user_list:
            if ip==user[1]:
                log_in_user(user[0])
                user_exists=True
                break
        if not(user_exists):
            name=input("Введите имя пользователя: ")
            add_user(ip,name,file)
    
def add_user(ip,name,file="users.txt"):
    """Добавить пользователя с данным именем и IP-адресом"""
    users_file=open(file,"a") 
    name.strip()
    users_file.write("{};{}".format(name,ip))
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
            
def log_in_user(name):
    print("Пользователь {} вошёл в систему".format(name))