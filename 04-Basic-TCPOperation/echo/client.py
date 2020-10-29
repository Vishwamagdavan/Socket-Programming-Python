import socket

server = socket.socket()
SERVER = socket.gethostname()
IP = socket.gethostbyname(SERVER)
PORT = 5050

print(f"SERVER:{SERVER} IP:{IP}")
ADDR=(SERVER,PORT)
server.connect(ADDR)

message=input("Enter the Message:")
server.send(message.encode())
smessage = server.recv(1024).decode('utf-8')
print(smessage)
server.close