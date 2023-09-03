import socket
import pyperclip
import sys
import select
import time


def SimpleTCPServer():
    if not len(sys.argv) >= 3:
        print("""
    Invalid Args...
    Usage:
        Your/Path/copyMeICopyYou/client.py <server ip> <port>

    Use command Your/Path/copyMeICopyYou/client.py --help
    to display available commands.
            """)
        quit()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = sys.argv[1]
    port = int(sys.argv[2])
    s.connect((host, port))

    msg = "Hello World"
    s.send(msg.encode('utf-8'))
    msgRecv = msgRecv = s.recv(1000000)
    pyperclip.copy(msgRecv.decode('utf-8'))
    pastedValue = pyperclip.paste()
    cacheDict = {"key": pastedValue}
    timeout = 2

    while True:
        while True:
            pastedValue = pyperclip.paste()  # Determine cur and prev paste

            # Check if previous copied value equals the current value
            if pastedValue == cacheDict['key']:
                # Set a timeout of 2 seconds for receiving data
                s.settimeout(2)

                while True:
                    try:
                        # Receive data from the server
                        msgRecv = s.recv(1000000)

                        if not msgRecv:
                            # No data received, stop listening
                            if "--debug" in sys.argv:
                                print("No data received, stopped listening")
                            break

                        # Process the received message
                        if "--debug" in sys.argv:
                            print("Received message:", msgRecv.decode('utf-8'))
                        pyperclip.copy(msgRecv.decode('utf-8'))

                    except socket.timeout:
                        # Timeout occurred, stop listening
                        if "--debug" in sys.argv:
                            print("Timeout occurred")
                        break

                if "--debug" in sys.argv:
                    print("Restarting loop...")
                pass
            else:
                try:
                    if "--debug" in sys.argv:
                        print("Copied new value...")

                    pastedValue = pyperclip.paste()  # paste
                    cacheDict['key'] = pastedValue
                    s.send(str(pastedValue).encode('utf-8'))  # send copied msg
                    msgRecv = s.recv(1000000)
                    pyperclip.copy(msgRecv.decode('utf-8'))
                    pastedValue = pyperclip.paste()  # paste
                    pastedValue = pastedValue  # redefine pastedValue
                except Exception as e:
                    continue
    if "--debug" in sys.argv:
        print("breaking from main loop...")


SimpleTCPServer()
