import socket


#настройки
port=9100
ip='localhost'


print(f'Запуск клиента на Python Socket. By Igor Stepanov (PI18-2). Ver. 0.0.1')
sock = socket.socket()  #общее для клиента и сервера
print(f'Подключаюсь к адресу {ip} и порту {port}...')
sock.connect((ip,port))    #подключение к порту 9100

print(f'Готово! Введите отправляемое сообщение!')
data = input() #получить строку с клавиатуры
print('Отправляю Ваше сообщение на сервер...')
sock.send(data.encode()) #Отправить строку на сервер

print('Получаю ответ от сервера...')
answer = sock.recv(1024)    #получить ответ от сервера
print('Соединение закрыто!')
sock.close()    #закрыть соединение

print('Вот что ответил сервер:')
print(answer.decode())   #вывести ответ сервера

print('\n\n\nКонец программы')
wait = input()