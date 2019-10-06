import socket
sock = socket.socket()
while True:
       host_name = input('Введите имя хоста или его адрес:(например localhost) ')
       if host_name == 'localhost':
              hosst_name='127.0.0.1'
              break
       host_ad=host_name.split('.')
       if (0<int(host_ad[0])<255) and (0<int(host_ad[1])<255) and (0<int(host_ad[2])<255) and (0<int(host_ad[3]<255)):
              break
       else:
              print('Неверный формат адреса')
while True:
       port=int(input('Введите порт :'))
       if 1024<=port<=65525:
              break
       else:
              print('Ошибка.Попробуйте еще раз ввести порт')
sock.bind(('', port))             
print(f'Слушаю ваш порт {port}')
sock.listen(1)
conn, addr = sock.accept()
print('Подключаюсь и вывожу адрес..',addr)
while True:
        msg = conn.recv(1024)
        print(msg.decode())
        if msg.decode() == 'exit':
            break
conn.close()
print('Соединение с клиентом закрыто')
