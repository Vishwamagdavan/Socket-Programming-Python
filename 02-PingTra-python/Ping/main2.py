from pythonping import ping
def checkping(hostname):
    ping(hostname, verbose=True)
hostname=input('Enter the Host:')
checkping(hostname)


