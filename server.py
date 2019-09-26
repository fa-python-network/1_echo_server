import socket
s=socket.socket()

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

port=check_port(input('Введите номер порта '))
s.bind(('',port))
s.listen(1)


while True:
	msg=''
	conn,address=s.accept()
	data=conn.recv(1024)
	msg=data.decode()
	print(msg)
conn.close()
	
