import socket
from time import sleep
print("введите адрес хоста и номер порта")
adress = input()
port = int(input())
if not adress:
  adress  = '10.38.165.12'
if not port:
  port = 9090
sock = socket.socket()
sock.connect((adress, port))
ex = True
while ex:
  msg = input()
  if msg == "exit":
    ex = False
  sock.send(msg.encode())
  data = sock.recv(1024)
  print(data.decode())
sock.close()  
  

  
  
