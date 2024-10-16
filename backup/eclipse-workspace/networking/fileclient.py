import socket

s = socket.socket()

s.connect(('localhost',4000))

fileName = input("Enter a filename")
s.send(fileName.encode())

content = s.recv(1024)

print(content.decode())
    
s.close()
