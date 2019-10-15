import socket

sock = socket.socket()

cod=int(input("Введите номер порта:"))

sock.connect(('localhost',cod))
sock.send(b"Hello,dear!")
msg="hello"
sock.send(msg.encode())

response = sock.recv(1024).decode()
print(response)
while True:
  s = str(input('Tell somethink:'))
  if s == 'exit':
    sock.close()
    break
