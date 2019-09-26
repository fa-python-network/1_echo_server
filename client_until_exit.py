import socket


#настройки
port=9100
ip='localhost'


print(f'Для прекращения работы напишите EXIT!')
sock = socket.socket()  #общее для клиента и сервера
print(f'Подключаюсь к адресу {ip} и порту {port}...')
sock.connect((ip,port))    #подключение к порту 9100

while True:
    print(f'Готово! Введите отправляемое сообщение!')
    data = input() #получить строку с клавиатуры
    
    if data == 'exit':      #если клиенту надоест
        break
    
    print('Отправляю Ваше сообщение на сервер...')
    sock.send(data.encode()) #Отправить строку на сервер
    
    print('Получаю ответ от сервера...')
    answer = sock.recv(1024)    #получить ответ от сервера
    print('Вот что ответил сервер:')
    print(answer.decode())   #вывести ответ сервера


print('Соединение закрыто!')
sock.close()    #закрыть соединение

print('\n\n\nКонец программы')
wait = input()