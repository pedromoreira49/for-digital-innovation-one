import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

print('SUCESSO')

host = 'localhost'
port = 5433
message = 'hello world'

try:
	print("Client: " + message)
	s.sendto(message.encode(), (host, port))
	datas, server = s.recvfrom(4096)
	datas = datas.decode()
	print("Server: " + datas)
finally:
	print("End connection")
	s.close()