import socket
from time import sleep

sock = socket.socket()
sock.connect(('10.38.165.12', 9090))
ex = True
while ex:
  msg = input()
  if msg == "exit":
    ex = False
  sock.send(msg.encode())
  data = sock.recv(1024)
  print(data.decode())
sock.close()  
  

  
  
