import socket


host = 'localhost'
port = 4000

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))
print("Server is listening on port:",port)
s.listen(1)

c,addr = s.accept()

fileName = c.recv(1024)
try:
    f = open(fileName,"rb")
    content = f.read()
    c.send(content)
    f.close()
except FileNotFoundError:
    c.send(b"File doe not exist")
c.close()