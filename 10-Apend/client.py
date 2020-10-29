import socket

HEADER=64
PORT=5050
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT='utf-8'
DISCONNECTED_MSG="!DISCONNECTED"
ADDR=(SERVER,PORT)

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

inp=True
while inp:
    msg=input()
    if msg=="EXIT":
        inp=False
    send(msg)

send(DISCONNECTED_MSG)