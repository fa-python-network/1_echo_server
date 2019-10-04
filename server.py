import socket
import port_functions

s=socket.socket()
port=port_functions.check_port(input('Введите номер порта '), 9090)
port_functions.change_port(port,s)
#s.bind(('',port))
s.listen(1)

while True:
	msg=''
	conn,address=s.accept()
	data=conn.recv(1024)
	msg=data.decode()
	print(msg)
conn.close()
	
