import sys 
from socket import * 
from threading import Thread
from HttpRequest import httpReq

serverSocket = socket(AF_INET, SOCK_STREAM)

portNum = 12000
threadNum = 1
serverSocket.bind(("", portNum))
serverSocket.listen(1)



while True:
    print('The server is ready to receive')    
    connectionSocket, addr = serverSocket.accept()
    request = Thread(target=httpReq, args=(connectionSocket, threadNum))
    print(f"\nThread {threadNum} started\n")
    request.start()
    threadNum += 1


serverSocket.close()
sys.exit()