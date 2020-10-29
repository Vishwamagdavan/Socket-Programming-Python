import socket
import pickle


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 5050))
server.listen(5)
arptable={}
print("1.Enter Mac/StringLen/IP\n2.Exit")
choice=int(input("Enter the Choice:"))
while choice==1:
    macAddress=input("Enter the Mac Address:")
    Stringlenth=int(input("Enter the String Length:"))
    IpAddress=input("Enter the IP Address:")
    arptable[macAddress]=IpAddress
    choice=int(input("Enter the Choice:"))
for key,value in arptable.items():
    print(f"{key}.{value}")

conn, address = server.accept()
print(f"Connection from {address} has been established.")
data = pickle.dumps(arptable)
conn.send(data)
conn.send("ARP Table Fetched!".encode('utf-8'))