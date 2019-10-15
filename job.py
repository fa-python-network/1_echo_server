import socket

f=open('t.txt','w')
f.write("Открываем сервер")
sock = socket.socket()
  while True:
  sock.bind(("", 9093))
  print("Прослушиваем порт")
  sock.listen(1)

  f.write("Подключаем клиента")
  conn, addr = sock.accept()
  print(addr)

  f.write("Принемаем данные от клиента")
  data=conn.recv(1024)
  print(data.decode())
  if (data.decode() == "Exit"0):
    f.write("Отключаем клиента. Пока-пока")
    conn.close
  
  f.write("Отправляем данные клиенту")
  conn.send(b"hi")
  conn.send(('\nIP {}'.format(addr[0])).encode())
f.write("Стопаем сервак")
sock.close
