def check_port(port):
	default=9090
	port=int(port)
	if 1024<port<65536:
		pass
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