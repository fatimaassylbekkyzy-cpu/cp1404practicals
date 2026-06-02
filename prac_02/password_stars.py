MIN_PASSWORD_LENGTH = 8

password = input("Password: ")
while len(password) < MIN_PASSWORD_LENGTH:
	print("Password doesn't meet a minimum length of 8 characters.")
	password = input("Password: ")
print('*' * len(password))
