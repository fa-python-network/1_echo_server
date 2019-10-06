import socket
import datetime



logs=[]



sock = socket.socket()

#цикл while отвечает за bind свободного порта
a=0
sckt=9090
while  a!=1 and sckt<15000:
	try:
		sock.bind(('', sckt))
		a+=1
		print("***сервер зарезервировал порт N"+str(sckt))
		logs.append(str(datetime.datetime.now())+" зарезервировван порт N")
	except:
		sckt+=1
		print(sckt)
	

print("***Сервер запущен***")
logs.append(str(datetime.datetime.now())+" запущен сервер")

sock.listen(1)



command=''
while command!="stop":
	
	sock.listen(1)
	print("***Ожидание подключения***")
	conn, addr = sock.accept()
	logs.append(str(datetime.datetime.now())+" Установлено соединение с "+addr[0])
	print ('***Установлено соединение с:', addr,'***')

	while True:
	    data = conn.recv(1024)
	    msg=''
	    if not data:
	        break
	    msg+=data.decode() 
	    conn.send(data.upper())
	    print(msg)
	logs.append(str(datetime.datetime.now())+" пользователь "+ addr[0]+" отключился")
	print("***Пользователь "+addr[0]+" отключился***")
	print("***Продолжить или отключить сервер?***")
	command=input()
logs.append(str(datetime.datetime.now())+" сервер завершает работу")
logs.append("---"*20)

try:
	f=open('logs.txt','a')
	for i in logs:
		f.write(i+'\n')
except:
	f=open('logs.txt','w')
	for i in logs:
		f.write(i+'\n')
f.close()
conn.close()
