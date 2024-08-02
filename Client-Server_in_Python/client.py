import socket
import pickle


HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while True:

    full_message = b''
    new_message = True
    while True:
        message = s.recv(16)
        if new_message:
            print(f"New message length: {message[:HEADERSIZE]}")
            message_length = int(message[:HEADERSIZE])
            new_message = False

        # full_message += message.decode("utf-8")
        full_message += message

        if len(full_message) - HEADERSIZE == message_length:
            print("Full message received!")
            print(full_message[HEADERSIZE:])

            d = pickle.loads(full_message[HEADERSIZE:])
            print(d)

            new_message = True
            full_message = ''

    print(full_message)
