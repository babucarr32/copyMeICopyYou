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
            pyperPaste = pyperclip.paste() # Determine cur and prev paste

            if pyperPaste == newPyper: # if pastes are the same pass
                pass
            else:
                pyperPaste = pyperclip.paste() # paste
                pyperCopy = pyperclip.copy(pyperPaste) # copy paste
                s.send(str(pyperCopy).encode('utf-8')) # send copied msg
                newPyper = pyperPaste # redefine newPyper
                break
        print(msg_recv.decode("utf-8"))
SimpleTCPServer()
Help
decode
decode
redefine