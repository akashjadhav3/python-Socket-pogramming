import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 1255

s.connect((host, port))
msg = "hi this is client sending msg"

s.send(msg.encode('utf-8'))
s.close()
