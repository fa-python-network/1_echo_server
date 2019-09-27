import socket


#настройки
port=9100
ip='localhost'


print(f'Для прекращения работы напишите EXIT!')
sock = socket.socket()  #общее для клиента и сервера
print(f'Подключаюсь к адресу {ip} и порту {port}...')
sock.connect((ip,port))    #подключение к порту 9100

print('Получаю ответ от сервера...')
answer = sock.recv(1024)    #получить ответ от сервера

if answer.decode() == 'give_me_name':
	print('Enter your name')	#спросить имя, если новенький
	newname = input()
	sock.send(newname.encode())
	print('Added new account. Restart client!')
else:
	print(answer.decode())


print('Соединение закрыто!')
sock.close()    #закрыть соединение

print('\n\n\nКонец программы')
wait = input()