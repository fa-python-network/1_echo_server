import socket
import logging
logging.basicConfig(filename='sample.log', level=logging.INFO)


sock = socket.socket()

port = 9090

while port !=65525:
	try:
		sock.bind(('',port))
		print('The port is: {}'.format(port))
		break
	except:
		print('The port is not available. Cheacking a new one...')
		port+=1


sock.listen(1)
logging.info('listening')

while True:
	file=open('manual.txt', 'r')
	conn,addr=sock.accept()
	print('Now connected to {}'.format(addr[0]))
	f=0
	for line in file:
		l=line.strip()
		if str(addr[0]) in l:
			name=l.split('-')[1]
			conn.send('hi,{}'.format(name).encode())
			f=1
			break
	if f==0:
		file=open('manual.txt', 'a+')
		conn.send('Create your name'.encode())
		got_name=conn.recv(1024).decode()
		file=open('manual.txt', 'a')
		file.write('\n{} - {}'.format(addr[0],got_name.decode()))
		file.close()
			


	msg = ''
	while True:
		data = conn.recv(1024)
		logging.info('got a message')
		if not data:
			break
		print('The messages of {} are [ {} ]'.format(addr[0],data.decode()))


logging.info('done')
conn.close()