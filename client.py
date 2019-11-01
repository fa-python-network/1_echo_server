# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 08:46:48 2019

@author: 187056
"""
import socket
sock=socket.socket()
while True:
       host_name = input('Введите имя хоста или его адрес:(например localhost) ')
       if host_name == 'localhost':
              hosst_name='127.0.0.1'
              break
       host_ad=host_name.split('.')
       if all (0 <= int(item) <=255 for item in host_ad):
              break
       else:
              print('Неверный формат адреса')
while True:
       port = int(input('Введите значение порта от 1024 до 65525: '))
       if 1024 <= int(port) <= 65525:
              break
       else:
              print('Неправильный номер порта ')
              break
sock.setblocking(1)
print(f'Идет подключение к хосту {host_name} и порту {port} ')
print('Идет подлючение к порту..')
sock.connect((host_name,port)) 
while True:
    data = sock.recv(1024)
    print(data.decode())
    if data.decode() == 'Как вас зовут?':
        username = input()
        sock.send(username.encode())
    
    if data.decode() == 'Создайте свой пароль':
        password=input()
        if password != '':
            sock.send(password.encode())
    if data.decode() == 'Введите пароль: ' or data.decode()== 'Ошибка в пароле':
        password=input()
        sock.send(password.encode())
    if "Добро пожаловать" in data.decode():
        break
while True:
        msg = input('Введите свое сообщение, если вы хотите окончить работу, то вводите exit: ')
        sock.send(msg.encode())
        if msg == 'exit':
            break
print('Сообщение отправлено ')
sock.close()
