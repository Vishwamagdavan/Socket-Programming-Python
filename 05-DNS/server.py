import socket

server = socket.socket()
SERVER = socket.gethostname()
IP = socket.gethostbyname(SERVER)
PORT = 5050
ADDR=(SERVER,PORT)
server.bind(ADDR)
print(f"SERVER:{SERVER} IP:{IP}") 
server.listen(1)
conn, addr = server.accept()
domain = conn.recv(1024).decode('utf-8')
domaintohost=socket.gethostbyname(domain)
print(f"Domain: {domain}\nIP:{domaintohost}")
conn.send(domaintohost.encode('utf-8'))
print("SHUTING DOWN THE SERVER~!")
conn.close
server.close
