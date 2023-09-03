import socket
import threading
import sys
import Banner
import getIp

print(Banner.banner)

ipAddress = getIp.get_network_ip()


def handle_client(client, clients):
    while True:
        try:
            # Receive message
            msgRecv = client.recv(1000000)
            # Break if no message received
            if not msgRecv:
                break

            # Decode the message received
            msg = msgRecv.decode('utf-8')
            if "--debug" in sys.argv:
                print("Message Received is: ", msg)

            # Send the message to all clients connected
            for otherClient in clients:
                if otherClient != client:
                    otherClient.send(msg.encode('utf-8'))
        except Exception as e:
            if "--debug" in sys.argv:
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
    nums = [1, 2, 4]

    print(Banner.style.RESET)

    print(
        f"Connect to server using the ip: {Banner.style.CYAN}{ ipAddress}:{port}")
    print(Banner.style.RESET)
    print("Server is listening...")
    print(Banner.style.GREEN)

    while True:
        c, addr = s.accept()
        clients.append(c)

        if "--debug" in sys.argv:
            print(f"Got connection from {addr}")

        # Start a new thread to handle the client
        client_thread = threading.Thread(
            target=handle_client, args=(c, clients))
        client_thread.start()


if __name__ == "__main__":
    SimpleTCPServer()
