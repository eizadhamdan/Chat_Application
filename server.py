import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET corresponds to IPv4, SOCK_STREAM corresponds to TCP

s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    client_socket, address = s.accept()
    print(f"Connection from {address} has been established!")
    client_socket.send(bytes("Welcome to my server!", "utf-8"))
    client_socket.close()
