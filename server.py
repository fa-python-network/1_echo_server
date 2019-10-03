import socket
from loger import Logfile
from random import randint

def identification(c,ad):
    try:
        open('users.txt').close()
    except:
        open('users.txt','w').close()
    with open('users.txt','r', encoding="utf-8") as f:
        d=dict()
        d = dict(x.rstrip().split(None, 1) for x in f)
        x=d.get(ad[0],-1)
        if x!=-1:
            conn.send(x.encode())
        else:
            conn.send('Это неизвестный пользователь. Скажите мне ваше имя: '.encode())
            name = conn.recv(1024).decode()
            with open('users.txt','a', encoding="utf-8") as g:
                print(f"{ad[0]} {name}", file=g)
            


        

    




l = Logfile()
l.serverstart()
try:
    port=int(input("Ваш порт:"))
    if not 0 <= port <= 65535:
        raise ValueError
except ValueError:
        port = 9090

def random_free_port(p):
	try:
		sock = socket.socket()
		sock.bind(('',p))
		sock.close
		return p
	except:
		for _ in range(0, 65536):
			try:
				p=randint(0,65535)
				sock = socket.socket()
				sock.bind(('',p))
				sock.close
				return p
			except:
				continue    
port=random_free_port(port)          
print('Номер порта:',port)
while True:
    sock = socket.socket()
    sock.bind(('', port))
    sock.listen(1)
    conn, addr = sock.accept()
    f=identification(conn,addr)
    msg = '\nconeccted'
    data=list()
    print(msg)
    while True:
        findings = conn.recv(1024)
        if findings:
                data.append(findings.decode())
                print(data[-1])
        else:
            conn.close()
            break

print('\n'.join(data))


conn.close()
l.serverend()
