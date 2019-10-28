import socket
def sendstxt: #Функция для принятия сообщений
  data=conn.recv(1024)
  print(data.decode())   
f=open('t.txt','w') #Фаил со служебными сообщениями 
names=open('names.txt','w') #Фаил с именами
f.write("Открываем сервер")
b=false
sock = socket.socket()
  while True:
  i=9093
  sock.bind(("",i))
  f.write("Прослушиваем порт")
  while thutry:
    sock.listen(1)
  exept:
    while true:
      i=i+1
      sock.bind(("",i))
    Print("Номер порта:",i)
 
      
    
  f.write("Подключаем клиента")
  while true: #многопользовательский чат
    conn, addr = sock.accept()
    for lines in names: #моя странная реализация кукки
      if lines[1]==conn:
        print('Hello', lines[2])
        password=str(input(lines[2]," Enter your password:")
        While (password<>lines[3]):
          password=str(input(lines[2]," Your password is wrong. Enter it again:")
      i=1
   if i=0:
      name.write(input("Enter your name:")
     password=str(input("Enter your password:")
     password2=str(input("Enter your password again:")
      while (password1<>password2):
        password2=str(input("Error. Passwords in not shodatsya! Enter your password again:")
      names.write(password)
  

    f.write("Принемаем данные от клиента")
    data=conn.recv(1024)
    print(data.decode())
    if (data.decode() == "Exit"0):
      f.write("Отключаем клиента. Пока-пока")
      conn.close

    conn.sendstxt #выполняем функцию принятия сообщений от клиента

    f.write("Отправляем данные клиенту")
    conn.send(b"hi")
    conn.send(('\nIP {}'.format(addr[0])).encode())
  f.write("Стопаем сервак")
sock.close
