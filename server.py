import socket

SERVER_ADDRESS = ('', 3310)

server = socket.socket()
server.bind(SERVER_ADDRESS)
server.listen(5)
print("Ждём подключения клиента...")
while True:
    x, s = server.accept()
    data = x.recv(4096)
    l = data.decode("UTF-8")
    print("Получили от клиента:", l)
    if l == 'stop':
        print("Завершение")
        break
    data = data * 10
    x.send(data)
    x.close()