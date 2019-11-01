# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 08:54:53 2019

@author: 187056
"""
import socket
import csv
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
       if all (0 <= int(item) <=255 for item in host_ad):
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
while True:
    file=open('serv.log','a')             
    print(f'Слушаю ваш порт {port}')
    file.write(f'Слушаю ваш порт  {port} \n')
    sock.listen(1)
    conn, addr = sock.accept()
    print('Подключаюсь и вывожу адрес..',addr)
    file.write(f'Подключаюсь и вывожу адрес..{addr} \n')
    file.close()
    user=False
    usernames = open('username.csv','a')
    usernames.close()
    usernames = open('username.csv','r')
    for line in csv.reader(usernames):
        if line[0] == addr[0]:
            answ ='Введите пароль: '
            conn.send(answ.encode())
            while True:
                data = conn.recv(1024)
                password = data.decode()
                if line [2] == password:
                    answ = "Добро пожаловать," + line [1] + '!'
                    conn.send(answ.encode())
                    file = open('serv.log','a')
                    file.write('Вход выполнен успешно.Пароль введен верно')
                    file.close()
                    break
                else:
                    conn.send('В вашем пароле обнаружена ошибка.Попробуйте еще раз!')
                    file = open('serv.log','a')
                    file.write('Неверный пароль \n')
                    file.close()
                    
            user = True
            file = open('serv.log','a')
            file.write('Подключился известный пользователь \n')
        file.close()
        usernames.close()
    if user == False:
        file = open('serv.log','a')
        conn.send('Как вас зовут?'.encode())
        try:
            data = conn.recv(1024)
            name = data.decode()
            with open ('username.csv','a') as usernames:
                csv.writer(usernames).writerow([addr[0],name])
                usernames.close()
            file.write('Я добавил пользователя'+ name +'\n')
            file.close()
        except:
            name='Новый пользователь'
            conn.send('Возникла ошибка при вводе ваших данных.Вход произведен новым пользователем! \n'.encode())
            usernames = open ('username.csv','a')
            csv.writer(name).writerow([addr[0],name])
            usernames.close()
            file.write('Новый пользователеь в системе!')
        answ='Добро пожаловать,' + name 
        conn.send(answ.encode())
    while True:
        data=conn.recv(1024)
        password=data.decode()
        if line[2] == password:
            answ = "Добро пожаловать, " + line[1] + "!"
            conn.send(answ.encode())
            file = open('serv.log','a')
            file.write("Вход выполнен успешно: пароль верный.\n")
            file.close()
            break
    
        else:
        		conn.send("Неверный пароль. Попробуйте еще раз.")
        		file=open('serv.log','a')
        		file.write("Неверный пароль.\n")
        		file.close()
    
    while True:
            file = open('serv.log','a')
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
