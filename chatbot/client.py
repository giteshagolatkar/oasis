import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 5000

client.connect((host, port))

print("Connected to server.")

while True:
    message = input("You: ")
    client.send(message.encode())

    if message.lower() == "bye":
        break

    reply = client.recv(1024).decode()

    if reply.lower() == "bye":
        print("Server disconnected.")
        break

    print("Server:", reply)

client.close()
