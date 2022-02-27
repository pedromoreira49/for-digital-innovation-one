import socket
import sys

def main():
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
	except socket.error as err:
		print("Connection failed!")
		print("Error: {}".format(err))
		sys.exit()


	print("Success")


	host = input("Target address: ")
	port = input("Target port: ")

	try:
		s.connect((host, int(port)))
		print("Connection Success")
		s.shutdown(2)
	except socket.error as err:
		print("Failed!")
		print("Error: {}".format(err))
		sys.exit()


if __name__ == "__main__":
	main()