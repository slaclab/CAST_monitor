import socket


IP = '172.21.161.49'
PORT = 80
BUFFER_SIZE = 10*1024
CMD = b'*idn?'


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
s.send(CMD)
data = s.recv(BUFFER_SIZE)
s.close()

print("received data:", data)