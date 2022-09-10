import socket

SERVER_ADDRESS = ('localhost', 3310)

client = socket.socket()
client.connect(SERVER_ADDRESS)
client.send(bytes("5", encoding="UTF-8"))
data = client.recv(4096)
print(data.decode("UTF-8"))