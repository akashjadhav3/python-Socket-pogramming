import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 1255

s.bind((host, port))
s.listen(5)

socketClient , address = s.accept()
print("got connection from ",address)