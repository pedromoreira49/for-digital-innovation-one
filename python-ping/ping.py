import os

print("#" * 60)

ip = input("Informe o endereço ou url do algo: ")

os.system("ping {}".format(ip))

print("-" * 60)