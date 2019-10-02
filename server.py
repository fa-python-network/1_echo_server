import socket

log=''

while True:
	port = int(input('enter your port: '))
	if 1024<=port<=65525:
		break
	else:
		print('wrong port...')

sock = socket.socket()
sock.bind(('',port))
with open('log.txt', 'a') as handle:
	print('just started', file=handle)
log+='just started...'
sock.listen(1)
with open('log.txt', 'a') as handle:
	print('connected...', file=handle)

while True:
	conn,addr=sock.accept()
	print(addr)
	print('dead')
	log+='\nconnected...'

	msg = ''
	while True:
		data = conn.recv(1024)
		if not data:
			break
		with open('log.txt', 'a') as handle:
			print('got a message from client', file=handle)
		if 'exit' in input():
			conn.close()
		msg = data.decode()
		print(msg)


	#conn.send(data)
conn.close()