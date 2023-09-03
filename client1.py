import socket
import pyperclip
import sys
import select
import time
from Banner import style
import Banner


print(Banner.banner)


def SimpleTCPServer():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = input("Enter host Eg: 10.1.1.1 $ ")
        port = int(input("Enter port Eg: 55555 $ "))
        s.connect((host, port))
        print("""
            Connection successful...
            Setup the second computer to start sharing your clipboard.
            """)
    except Exception as e:
        print(f"""{style.RED}
    Failed to connect to server.{style.RESET}
    Invalid Args...{style.CYAN}
        Usage:
            Your/Path/copyMeICopyYou/client.py <server ip> <port>

        Use command Your/Path/copyMeICopyYou/client.py --help
        to display available commands.
        {style.RESET}{style.RED}
    Troubleshoot:{style.CYAN}
        1. Make sure server is running.
        2. Make sure you have python installed, if you are this as a script
            (.py) not as an executable.
        3. Make sure you your ip and port is set 
            to the ip displayed on the server.
            Example "🚀 Listening on 10.1.1.135:55555" means your command 
            your host is 10.1.1.135 and your port is 55555
        4. Make sure your port is an number(integer) with no trailing whitespaces.
        5. Make sure your are connected to the same network as the server.
        6. Make sure your not behind a firewall.

        Stop and restart to establish connection with Ctrl + c {style.RESET}
            """)
        time.sleep(60*5)
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
                            print("Received message:",
                                  msgRecv.decode('utf-8'))
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
                    s.send(str(pastedValue).encode(
                        'utf-8'))  # send copied msg
                    msgRecv = s.recv(1000000)
                    pyperclip.copy(msgRecv.decode('utf-8'))
                except Exception as e:
                    continue
    if "--debug" in sys.argv:
        print("breaking from main loop...")


SimpleTCPServer()
