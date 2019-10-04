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
            
    
            