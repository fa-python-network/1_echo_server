import socket
sock = socket.socket()
while True:
       file = open('serv.log','a')
       host_name = input('Введите имя хоста или его адрес:(например localhost) ')
       file.write('Запрашиваю адрес хоста...\n')
       if host_name == 'localhost':
              hosst_name = '127.0.0.1'
              file.write(f'Введите адрес хоста {host_name}: \n')
              file.close()
              break
       if host_name == '':
              file.write('Адрес хоста отсутствует..проверьте свои данные!')
              file.close()
              break
       host_ad=host_name.split('.')
       if (0<int(host_ad[0])<255) and (0<int(host_ad[1])<255) and (0<int(host_ad[2])<255) and (0<int(host_ad[3]<255)):
              file.write(f'Введите адрес хоста: {host_name} \n')
              file.close()
              break
       else:
              print('Неверный формат адреса')
              file.write('Неверный формат адреса \n ')
while True:
       file=open('serv.log','a')
       port=int(input('Введите значение порта от 1024 до 65525:'))
       file.write('Запрашиваю данные о номере порта.. \n')
       if 1024<=int(port)<=65525:
              file.write(f'Номер порта: {port} \n ')
              file.close()
              break
       else:
              print('Ошибка (неверный номер порта).Попробуйте еще раз ввести порт')

while True:
    try:
        sock.bind(('', port))
        break
    except:
        if 1024<=port<=65525:
                port+=1
        else:
                port=9090

file=open('serv.log','a')             
print(f'Слушаю ваш порт {port}')
file.write(f'Слушаю ваш порт  {port} \n')

sock.listen(1)
conn, addr = sock.accept()

print('Подключаюсь и вывожу адрес..',addr)
file.write(f'Подключаюсь и вывожу адрес..{addr} \n')
file.close()

while True:
        file=open('serv.log','a')
        msg = conn.recv(1024)
        print(msg.decode())
        if msg.decode() == 'exit':
            file.write(f'Попращался с {addr} \n ')
            file.close()
            break
        file.write(f'Принял сообшение {msg} и жду следующее \n ')
        file.close()
conn.close()
print('Соединение с клиентом закрыто')
