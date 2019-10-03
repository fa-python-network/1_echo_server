import socket
import logging

#Создается и используется объект логгирования
logger = logging.getLogger("serverLogger")
logger.setLevel(logging.INFO)
fh = logging.FileHandler("server.log")
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

logger.info("Start server")


sock = socket.socket()
sock.bind(('127.0.0.1', 9090))
sock.listen(0)
conn, addr = sock.accept()
logger.info(f"Connect client {addr[0]}:{addr[1]}")
print(addr)

msg = ''

while True:
	data = conn.recv(1024)
	if not data:
		conn, addr = sock.accept()
	elif data == 'exit':
		logger.info(f"Disconnect client {addr[0]}:{addr[1]}")
		conn.close()
	else:
		logger.info(f"From client {addr[0]}:{addr[1]} - {data}")
		conn.send(data.upper())

sock.close()
