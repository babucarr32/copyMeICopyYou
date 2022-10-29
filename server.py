import socket
import pyperclip

def SimpleTCPServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host =  ""
    port = 55555
    s.bind((host, port))
    s.listen()
    clients = []

    print("Listening...")
    while True:
        # accept 
        c, addr =  s.accept()
        clients.append(c)
        print(f"Got connection from {addr}")
        # recieve message
        msg_recv = c.recv(1000000)
        # copy message
        pyperclip.copy(msg_recv.decode('utf-8'))
        msg = input("Enter msg: ")
        for client in clients:
            client.send(msg.encode('utf-8'))
SimpleTCPServer()
