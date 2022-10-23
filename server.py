import socket

def SimpleTCPServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host =  ""
    port = 55555
    s.bind((host, port))
    s.listen()

    print("Listening...")
    while True:
        # accept 
        c, addr =  s.accept()
        print(f"Got connection from {addr}")
        # recieve message
        msg_recv = c.recv(1000000)
        for client in addr:
            c.send(f"hello world got connection from {addr}".encode('utf-8'))
SimpleTCPServer()