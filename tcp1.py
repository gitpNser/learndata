import socket

# creat a socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# creat connection

s.connect(('www.sina.com.cn', 80))

# send data

s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# collect data

buffer = []

while True:
	# 1k byte each time
	d = s.recv(1024)
	
	if d:
		
		buffer.append(d)
		
	else:
	
		break
		
data = b''.join(buffer)

# close the socket

s.close()

# separat the Headers and the html

header, html = data.split(b'\r\n\r\n', 1)

print(header.decode('utf-8'))

with open('sina.html', 'wb') as f:

	f.write(html)
	
