import os
def checkping(hostname):
    comandline="ping "+hostname
    print(f"{os.system(comandline)}")

hostname=input('Enter the Host:')
checkping(hostname)