import socket

print("Открываем сервер")
sock = socket.socket()
  while True:
  sock.bind(("", 9093))
  print("Прослушиваем порт")
  sock.listen(1)

  print("Подключаем клиента")
  conn, addr = sock.accept()
  print(addr)

  print("Принемаем данные от клиента")
  data=conn.recv(1024)
  print(data.decode())
  if (data.decode() == "Exit"0):
    print("Отключаем клиента. Пока-пока")
    conn.close
  
  print("Отправляем данные клиенту");
  conn.send(b"hi")
  conn.send(('\nIP {}'.format(addr[0])).encode())
print("Стопаем сервак")
sock.close
