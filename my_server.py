import socket
while True:
      port=int(input('Введите порт :'))
      if 1024<=port<=65525:
              break
      else:
              print('Ошибка.Попробуйте еще раз ввести порт')

sock = socket.socket()
sock.bind(("", port))
sock.listen(1)
while True:
      conn,addr = sock.accept() #принимаем сокет и адрес
      print('Вывожу адрес..')
      print(addr)

msg = ''

while True:
      data = conn.recv(1024)
      if not data:
              break
msg = data.decode()
conn.send(data)
conn.close()


print('Соединение с клиентом закрыто')
