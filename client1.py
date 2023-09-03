import socket
import pyperclip
import sys
import select
import time

def SimpleTCPServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "10.1.1.135"
    port = 55555
    s.connect((host, port))

    msg = "Hello World"
    s.send(msg.encode('utf-8'))
    msg_recv = msg_recv = s.recv(1000000)
    pyperCopy = pyperclip.copy(msg_recv.decode('utf-8'))
    newPyper = pyperclip.paste()
    pasteDict = {"key": newPyper}
    timeout = 2

    while True:
        # check for clipboard
        print("Checking...")
        while True:
            pyperPaste = pyperclip.paste() # Determine cur and prev paste

            if pyperPaste == pasteDict['key']: # if pastes are the same pass
                s.settimeout(2)  # Set a timeout of 2 seconds for receiving data

                while True:
                    try:
                        # Receive data from the server
                        msg_recv = s.recv(1000000)

                        if not msg_recv:
                            # No data received, stop listening
                            print("No data received, stop listening")
                            break

                        # Process the received message
                        print("Received message:", msg_recv.decode('utf-8'))
                        pyperclip.copy(msg_recv.decode('utf-8'))

                    except socket.timeout:
                        # Timeout occurred, stop listening
                        print("Timeout occured")
                        break


                print("passing.....", pasteDict)
                pass
            else:
                try:
                    print("Different.....")
                    pyperPaste = pyperclip.paste() # paste
                    pasteDict['key'] = pyperPaste
                    s.send(str(pyperPaste).encode('utf-8')) # send copied msg
                    msg_recv = s.recv(1000000)
                    pyperclip.copy(msg_recv.decode('utf-8'))
                    pyperPaste = pyperclip.paste() # paste
                    newPyper = pyperPaste # redefine newPyper
                except Exception as e:
                    continue
        print("breaked")
        print(pyperPaste)
    
SimpleTCPServer()
