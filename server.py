import socket
import logging
logging.basicConfig(filename='sample.log', level=logging.INFO)
file=open('manual.txt', 'r')

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
	conn,addr=sock.accept()
	print(addr[0])

	for line in file:
		l=line.strip()
		if str(addr[1]) in l:
			name=l.strip('-')[1]
			print('hi,{}'.format(name))
		else:
			file.close()
			ask_name='enter your name'
			conn.send(ask_name.encode())
			got_name=conn.recv(1024)
			file=open('manual.txt', 'a')
			file.write('{addr[1]} - {got_name}')
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