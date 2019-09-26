import socket
import re       #будем проверять айпишник

def set_ip_and_port(user_ip='localhost',user_port=9100):
    global port, ip     #будем менять глобальные переменные
    
    try:
        if int(user_port) > 1024 and int(user_port) < 65000:
            port = int(user_port)
        else:
            port = 9100
    except:
        port = 9100
        
        
    checkip = re.search('^(25[0-5]|2[0-4][0-9]|[0-1][0-9]{2}|[0-9]{2}|[0-9])(\.(25[0-5]|2[0-4][0-9]|[0-1][0-9]{2}|[0-9]{2}|[0-9])){3}$', user_ip, flags=re.IGNORECASE)
        
    if user_ip == 'localhost' or checkip is not None:     #если айпи валидный
        ip = user_ip
    else:
        ip = 'localhost'
    return

#настройки
port=None
ip=None


print('Введите IP:')
user_ip = input()
print('Введите порт:')
user_port = input()

set_ip_and_port(user_ip=user_ip,user_port=user_port)  #пробуем применить параметры пользователя

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