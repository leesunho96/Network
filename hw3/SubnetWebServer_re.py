import sys
from socket import *
from threading import Thread
from HttpRequest import httpReq
from struct import unpack

def atol(a):
    return unpack(">L", inet_aton(a))[0]

serverSocket = socket(AF_INET, SOCK_STREAM)

portNum = 12000
threadNum = 1

serverSocket.bind(("", portNum))
serverSocket.listen(1)


while True:
    print('The server is ready to receive')
    connSocket, addr = serverSocket.accept()
    print(f"sender subnet address = {addr[0][:-2]}, host: {addr[0][-1]}")
    
    addrs = atol(addr[0])
    mask = atol("255.255.255.0")
    lo = atol("192.168.0.0")
    hi = atol("192.168.0.255")
    prefix = addrs & mask

    if (lo <= prefix <= hi):
        th = Thread(target=httpReq, args=(connSocket, threadNum))
        print(f"\nThread {threadNum} started\n")
        th.start()
        threadNum = threadNum + 1
    else:
        print(f"Access Failed, IP=({addr[0]})")
        continue
     

portNum.close()
sys.exit()