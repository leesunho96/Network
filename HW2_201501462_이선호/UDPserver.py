from socket import *

serverPort = 12001
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print ("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    decodedMessage = message.decode()
    print("Received from :" + clientAddress[0] + decodedMessage)
    serverSocket.sendto(decodedMessage.encode(), clientAddress)
