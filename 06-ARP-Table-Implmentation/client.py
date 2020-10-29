import socket
import pickle


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((socket.gethostname(), 5050))
data = server.recv(1024)
arptable=pickle.loads(data)
msg = server.recv(1024).decode('utf-8')
print(msg)
print("ARP Table:")
for key,value in arptable.items():
    print(f"{key}.{value}")
server.close

print("1.ARP\n2.RARP\n3.EXIT")
choice=int(input('Enter your Choice:'))
while choice!=3:
    if choice==1:
        mac=input('Enter Mac Address')
        print(arptable[mac])
    elif choice==2:
        ip=input("Enter IP:")
        for key,val in arptable.items():
            if(val==key):
                print(ip)
    choice=int(input('Enter your Choice:'))
