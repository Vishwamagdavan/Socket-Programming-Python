import time, socket
print("[Chat Room Created]")
time.sleep(1)

server = socket.socket()
SERVER = socket.gethostname()
IP = socket.gethostbyname(SERVER)
PORT = 5050
ADDR=(SERVER,PORT)
server.bind(ADDR)
print(f"SERVER:{SERVER} IP:{IP}")
name = input(str("Enter your name: "))   
server.listen(1)

print("[Waiting for the reponder!]")
conn, addr = server.accept()
print("Received connection from ", addr[0], "(", addr[1], ")")

s_name = conn.recv(1024).decode('utf-8')
print(s_name, "Chat is Live : Enter [quit] to stop")
conn.send(name.encode())

while True:
    message = input(str("Me : "))
    if message == "[quit]":
        message = "Left chat room!"
        conn.send(message.encode())
        break
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(s_name, ":", message)