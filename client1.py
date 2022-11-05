import socket
import pyperclip
import sys
import select

def SimpleTCPServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host =  "10.1.1.135"
    port = 55555
    s.connect((host, port))

    msg = "Hello World"
    s.send(msg.encode('utf-8'))
    msg_recv = msg_recv = s.recv(1000000)
    pyperCopy = pyperclip.copy(msg_recv.decode('utf-8'))
    newPyper = pyperclip.paste()

    while True:
        # check for clipboard
        # while True:
        #     pyperPaste = pyperclip.paste() # Determine cur and prev paste

        #     if pyperPaste == newPyper: # if pastes are the same pass
        #         pass
        #     else:
        #         pyperPaste = pyperclip.paste() # paste
        #         s.send(str(pyperPaste).encode('utf-8')) # send copied msg
        #         msg_recv = s.recv(1000000)
        #         pyperclip.copy(msg_recv.decode('utf-8'))
        #         pyperPaste = pyperclip.paste() # paste
        #         newPyper = pyperPaste # redefine newPyper
        #         break
        # print("breaked")
        # print(pyperPaste)
        sockets_list = [sys.stdin, s]
    
        """ There are two possible input situations. Either the
        user wants to give manual input to send to other people,
        or the server is sending a message to be printed on the
        screen. Select returns from sockets_list, the stream that
        is reader for input. So for example, if the server wants
        to send a message, then the if condition will hold true
        below.If the user wants to send a message, the else
        condition will evaluate as true"""
        read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
    
        for socks in read_sockets:
            if socks == s:
                msg = socks.recv(2048)
                pyperclip.copy(msg.decode('utf-8'))
                print (msg)
            else:
                pyperPaste = pyperclip.paste() # Determine cur and prev paste

                # if pyperPaste == newPyper: # if pastes are the same pass
                #     pass
                # else:
                # message = sys.stdin.readline()
                pasteMsg = pyperclip.paste()
                s.send(pasteMsg.encode('utf-8'))
                # sys.stdout.write("<You>")
                # sys.stdout.write(message)
                # sys.stdout.flush()
SimpleTCPServer()