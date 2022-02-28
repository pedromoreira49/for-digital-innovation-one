import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("SUCESS")

host = "localhost"
port = 5433

s.bind((host, port))

message = "hello client"

while 1:
	datas, end = s.recvfrom(4096)

	if datas:
		print("Server sending datas...")
		s.sendto(datas, (message.encode()), end)