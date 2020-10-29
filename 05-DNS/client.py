import socket

server = socket.socket()
SERVER = socket.gethostname()
IP = socket.gethostbyname(SERVER)
PORT = 5050

print(f"SERVER:{SERVER} IP:{IP}")
ADDR=(SERVER,PORT)
server.connect(ADDR)

domain=input("Enter the Domain:")
server.send(domain.encode())
ip = server.recv(1024).decode('utf-8')
print(ip)
server.close