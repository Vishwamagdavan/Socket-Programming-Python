import socket

server=socket.socket()
SERVER = socket.gethostbyname(socket.gethostname())
PORT=5050
ADDR=(SERVER,PORT)
print(SERVER)
server.connect(ADDR)
server.send(("Image beeing uploaded!").encode('utf-8'))
f=open('sample.jpg','rb')
print("Sending...")
file=f.read(1024)
while (file):
    print("Sending...")
    server.send(file)
    file=f.read(1024)
f.close()
print("Sent!")
print(server.recv(1024))
server.close
