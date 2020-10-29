import os
def checktracert(hostname):
    comandline="tracert "+hostname
    print(f"{os.system(comandline)}")

hostname=input('Enter the Host:')
checktracert(hostname)