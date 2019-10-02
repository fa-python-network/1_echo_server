import socket
from loger import Logfile
from random import randint

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
