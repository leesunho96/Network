import sys
from socket import *
from threading import Thread
from HttpRequest import httpReq

serverSocket = socket(AF_INET, SOCK_STREAM)

portNum = 12000
threadNum = 1
accessAddress = []


serverSocket.bind(("", portNum))
serverSocket.listen(1)

with open("subnet_list.txt") as file:
    lines = file.readlines()
    for line in lines:
        accessAddress.append(line[:-1])
file.close()
print(f"accessible Sub-network: {accessAddress}")


while True:
    print('The server is ready to receive')
    connectionSocket, addr = serverSocket.accept()
    print(f"source IP subnet address = {addr[0][:-2]}, host: {addr[0][-1]}")
    if not addr[0] in accessAddress:
        print(f"Access Denied, IP=({addr[0]})")
        continue

    th = Thread(target=httpReq, args=(connectionSocket, threadNum))
    print(f"\nThread {threadNum} started\n")
    th.start()
    threadNum = threadNum+1


serverSocket.close()
sys.exit()