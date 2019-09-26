import socket
from datetime import datetime

def check_port(port):
	default=9090
	if type(port)=='int':
		if 0<port<65536:
			pass
		else:
			port=default
	else:
		port=default
	return port

def check_host(host):
	if host=='localhost':
		return host
	else:
		valid=True
		l=host.split('.')
		if len(l)==4:
			for n in l:
				if 0<=int(n)<=255:
					pass
				else:
					valid=False
					break
		else:
			valid=False
	if not(valid):
		host='localhost'
	return host

host=check_host(input('Введите хост '))
port=check_port(input('Введите номер порта '))
msg=''
while True:
	s=socket.socket()
	s.connect((host,port))
	msg=input('Введите сообщение. Для выхода введите exit ')
	if(msg=='exit'):
		break
	s.send(msg.encode())
	f=open('log.txt','a')
	f.write('Лог создан: {}. Отправлено сообщение {} длиной {} символов. Порт {}, хост {}\n'.format(datetime.today(),msg,len(msg),port,host))
	f.close()