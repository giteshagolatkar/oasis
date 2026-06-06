import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 5000

server.bind((host, port))
server.listen(1)

print("Server is waiting for connection...")

client, address = server.accept()

print("Connected with:", address)

while True:
    message = client.recv(1024).decode()

    if message.lower() == "bye":
        print("Client disconnected.")
        break

    print("Client:", message)

    reply = input("You: ")
    client.send(reply.encode())

    if reply.lower() == "bye":
        break

client.close()
server.close()
