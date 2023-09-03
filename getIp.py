import socket


def get_network_ip():
    try:
        # Create a socket connection to a remote server (doesn't actually connect)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(0.01)

        # Connect to a remote server, doesn't have to be reachable
        sock.connect(("10.0.0.1", 1))

        # Get the network IP address from the socket's address
        networkIp = sock.getsockname()[0]

        return networkIp
    except Exception as e:
        return str(e)
