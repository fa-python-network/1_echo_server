import socket
from time import sleep
import re




def accept(adr, port):
    lst = [];
    if re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', adr).group(0) == adr:
        lst.append(adr);
    if re.match(r'\d{1,4}', port).group(0) == port:
        lst.append(port)
    return lst





mem = True
while mem:
    print("введите адрес хоста и номер порта")
    adress = input()
    port = input()
    if not adress:
        adress = '192.168.0.100'
    if not port:
        port = '9090'
    check = accept(adress, port)
    print(check)
    if len(check) == 2:
        mem = False

port = int(port)
sock = socket.socket()
sock.connect((adress, port))
print(sock.recv(1024))

ex = True
while ex:
    msg = input()
    if msg == "exit":
        ex = False
    sock.send(msg.encode())
sock.close()  
  

  
  
