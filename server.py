import socket
import time
import pickle


HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET corresponds to IPv4, SOCK_STREAM corresponds to TCP

s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    client_socket, address = s.accept()
    print(f"Connection from {address} has been established!")

    # msg = 'Welcome to the sever!'

    d = {1: "Hey", 2: "There"}
    msg = pickle.dumps(d)

    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg

    client_socket.send(msg)

    # while True:
    #     time.sleep(3)
    #     msg = f"The time is: {time.time()}"
    #     msg = f'{len(msg):<{HEADERSIZE}}' + msg
    #     client_socket.send(bytes(msg, "utf-8"))
