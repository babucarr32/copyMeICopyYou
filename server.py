# import socket
# import pyperclip

# def SimpleTCPServer():
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     host =  ""
#     port = 55555
#     s.bind((host, port))
#     s.listen()
#     clients = []

#     print("Listening...")
#     while True:
#         c, addr =  s.accept()
#         clients.append(c)
#         print(f"Got connection from {addr}")

#         if len(clients) == 2:
#             while True:
#                 print("Waiting to receive.....")
#                 msg_recv = c.recv(1000000)
#                 msg  = msg_recv.decode('utf-8')
                
#                 for client in clients:
#                     client.send(msg.encode('utf-8'))
#                     print(msg_recv)
#         else:
#             pass
# SimpleTCPServer()




import socket
import threading

def handle_client(client, clients):
    while True:
        try:
            msg_recv = client.recv(1000000)
            if not msg_recv:
                break

            msg = msg_recv.decode('utf-8')
            print("Message Received is: ", msg)

            for other_client in clients:
                if other_client != client:
                    other_client.send(msg.encode('utf-8'))
        except Exception as e:
            print(f"Error handling client: {str(e)}")
            break

    # Remove the client from the list
    clients.remove(client)
    client.close()

def SimpleTCPServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = ""
    port = 55555
    s.bind((host, port))
    s.listen()
    clients = []

    print("Listening...")
    while True:
        c, addr = s.accept()
        clients.append(c)
        print(f"Got connection from {addr}")

        # Start a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(c, clients))
        client_thread.start()

if __name__ == "__main__":
    SimpleTCPServer()
