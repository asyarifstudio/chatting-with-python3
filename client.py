
import socket

#configurasi client dan server
connectionSocket = socket.socket()
serverIP = "127.0.0.1"
serverPort = 2222

#menghubungi server
connectionSocket.connect((serverIP,serverPort))
print("terhubung dengan server")

#bagian chatting
while True:
    message = connectionSocket.recv(1024)
    print("pesan dari server : {}".format(message.decode("utf-8")))
    message = input("masukkan pesan anda : ")
    connectionSocket.send(message.encode())