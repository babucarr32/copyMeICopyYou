import socket
import pyperclip

def SimpleTCPServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host =  "10.1.1.135"
    port = 55555
    s.connect((host, port))

    msg = "Hello World"
    s.send(msg.encode('utf-8'))
    msg_recv = msg_recv = s.recv(1000000)
    pyperCopy = pyperclip.copy(msg_recv.decode('utf-8'))
    newPyper = pyperCopy

    while True:
        # check for clipboard
        while True:
            pyperPaste = pyperclip.paste()

            if pyperPaste == newPyper:
                pass
            else:
                s.send(pyperPaste.encode('utf-8'))
                break
        print(msg_recv.decode("utf-8"))
SimpleTCPServer()
