from socket import *
from time import sleep


def httpReq(inputSocket, threadNum):
    try:
        message = inputSocket.recv(2048).decode()
        print(message)       
        fileName = message.split()[1]
        print(fileName)
        myfile = open(fileName[1:], "rb")
        response = myfile.read()
        myfile.close()
        header = 'HTTP/1.1 200 OK\n'
        if fileName.endswith(".jpg"):
            fileFormat = "image/jpg"
        elif fileName.endswith(".gif"):
            fileFormat = "image/gif"
        elif fileName.endswith(".mp4"):
            fileFormat = "video/mp4"
        elif fileName.endswith(".wmv"):
            fileFormat = "video/wmv"
        elif fileName.endswith(".html"):
            fileFormat = "text/html"
        else:
            raise IOError

        header += f"Content-Type: {str(fileFormat)}\n\n"
        print(header)

        inputSocket.send(header.encode())
        inputSocket.send(response)
        inputSocket.close()

        for i in range(1, 5):
            sleep(1)
            print(f"thread {threadNum} is working {i}")

    except IOError:
       
        header = "HTTP/1.1 404 Not Found\n\n"
        response = "<html><head></head><body><h1>Error 404: File not found</h1><p>Python HTTP Server</p></body></html>".encode()

        print(header)
        inputSocket.send(header.encode())
        inputSocket.send(response)
        
        inputSocket.close()