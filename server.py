import socket
from loger import Logfile


l = Logfile()
l.serverstart()

try:
    port = int(input("Ваш порт: "))
    if not 0 <= port <= 65535:
        raise ValueError
        
except ValueError:
        port = 9090
        
while True:
	sock = socket.socket()
    sock.bind(('', port))
    sock.listen(1)
    conn, addr = sock.accept()
    msg = ''
    data = list()
    print('')
    
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
