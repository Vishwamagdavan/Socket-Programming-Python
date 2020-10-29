import socket

server=socket.socket()
SERVER = socket.gethostbyname(socket.gethostname())
PORT=5050
print(SERVER,PORT)
ADDR=(SERVER,PORT)
server.bind(ADDR)
server.listen(5)
conn,addr=server.accept()
filename=conn.recv(1024).decode('utf-8')
extension=conn.recv(1024).decode('utf-8')
f=open(filename+"01"+extension,'wb')
while True:
    print(f'[Connection Established!] from {addr}')
    print("Receving...")
    file=conn.recv(1024)
    while file:
        print("Receving..")
        f.write(file)
        file=conn.recv(1024)
    f.close()
    print("Done Receiving")
    conn.send(("File uploaded").encode('utf-8'))
    conn.close