import socket

#configurasi server
listenerSocket = socket.socket()
serverIP = "0.0.0.0"
serverPort = 2222

#binding socket dengan IP dan port
listenerSocket.bind((serverIP,serverPort))
#listener socket siap menerima koneksi 
listenerSocket.listen(0)
print("server menunggu koneksi dari client")

while True:
    #listener socket menunggu koneksi dari client, line di bawah ini bersifat 'blocking'
    #artinya, programmnya terhenti di sini sampai ada koneksi ke listenerSocket
    handler, addr = listenerSocket.accept()
    #jika sudah ada koneksi dari client, maka program akan jalan ke line ini
    print("sebuah client terkoneksi dengan alamat:{}".format(addr))

    #bagian chatting
    while True:
        message = input("masukkan pesan anda : ")
        handler.send(message.encode())
        message = handler.recv(1024)
        print("pesan dari client : {}".format(message.decode("utf-8")))
