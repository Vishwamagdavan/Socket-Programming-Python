import socket

server=socket.socket()
SERVER = socket.gethostbyname(socket.gethostname())
PORT=5050
print(SERVER,PORT)
ADDR=(SERVER,PORT)
server.bind(ADDR)

f=open('rec.jpg','wb')
server.listen(5)
while True:
    conn,addr=server.accept()
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