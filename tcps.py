import socket
import threading
import time

# define a tcplink funtion to handle TCP connection
def tcplink(sock, addr):
	print('Accept new connection from %s:%s...' % addr)
	sock.send(b'Welcome!')
	
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8') == 'exit':
			break
		sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
	
	sock.close()
	print('Connection from %s:%s closed.' % addr)

# creat a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind a socket number and listen
s.bind(('127.0.0.1', 9999))
s.listen(5)
print('Waiting for connection...')

# set a loop to wait the request from client and setup a socket:
while True:
	# receive a new connection
	sock, addr = s.accept()
	# creat a new threading to hanle TCP connection by using function(tcplink)
	t = threading.Thread(target=tcplink, args=(sock, addr))
	t.start()