from socket import *
import time

serverName = '192.168.0.102'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.settimeout(1)
clientSocket.connect((serverName,serverPort))

with open("test.jpg") as file:
    sentence = file
file.close()

clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(2048)
      

clientSocket.close()
