import hashlib

file1 = 'file1.txt'
file2 = 'file2.txt'

hash1 = hashlib.new('ripemd160')

hash1.update(open(file1, 'rb').read())

hash2 = hashlib.new('ripemd160')

hash2.update(open(file2, 'rb').read())

if hash1.digest() != hash2.digest():
	print(f'File 1: {file1} é diferente do file 2: {file2}')
	print("Hash 1: ", hash1.hexdigest())
	print("Hash 2: ", hash2.hexdigest())
else:
	print(f'File 1: {file1} é igual ao file 2: {file2}')
	print("Hash 1: ", hash1.hexdigest())
	print("Hash 2: ", hash2.hexdigest())