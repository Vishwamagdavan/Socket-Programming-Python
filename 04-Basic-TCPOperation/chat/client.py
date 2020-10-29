import time, socket, sys

print("[Chat Room Created]")
time.sleep(1)


server = socket.socket()
SERVER = socket.gethostname()
IP = socket.gethostbyname(SERVER)
PORT = 5050


print(f"SERVER:{SERVER} IP:{IP}")
name = input(str("Enter your name: "))
ADDR=(SERVER,PORT)

print(f"Connecting SERVER:{SERVER} PORT:{PORT}")
time.sleep(1)
server.connect(ADDR)
print("Connected..")

server.send(name.encode())
s_name = server.recv(1024).decode('utf-8')
print(s_name, "Chat is Live : Enter [quit] to stop")

while True:
    message = server.recv(1024).decode('utf-8')
    print(s_name, ":", message)
    message = input(str("Me : "))
    if message == "[quit]":
        message = "Left chat room!"
        server.send(message.encode())
        break
    server.send(message.encode())