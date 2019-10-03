import socket
import logging
logging.basicConfig(filename='sample.log', level=logging.INFO)


sock = socket.socket()

port = 9090

while port !=65525:
	try:
		sock.bind(('',port))
		print(port)
		break
	except:
		print('try again')
		port+=1


sock.listen(1)
logging.info('listening')

while True:
	file=open('manual.txt', 'r')
	conn,addr=sock.accept()
	print(addr[0])
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
		ask_name='create your name'
		conn.send(ask_name.encode())
		got_name=conn.recv(1024)
		got_name.decode()
		file=open('manual.txt', 'a')
		file.write('\n{} - {}'.format(addr[0],got_name.decode()))
		file.close()
			


	msg = ''
	while True:
		data = conn.recv(1024)
		if not data:
			break
		logging.info('got a message')
		if 'exit' in input():
			conn.close()
		msg = data.decode()
		print(msg)

logging,info('done')
conn.close()