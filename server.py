import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(0)
conn, addr = sock.accept()
print(addr)

msg = ''

while True:
    findings = conn.recv(1024)
    if findings:
        data.append(findings.decode())
    else:
        conn.close()
        break
data='\n'.join(data)
print(data)

print(msg)

conn.close()
