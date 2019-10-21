import socket
from datetime import datetime
import port_functions

host=port_functions.check_host(input('Введите хост '))
port=port_functions.check_port(input('Введите номер порта '), 9090)
msg=''
if (port_functions.check_user(host)):
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