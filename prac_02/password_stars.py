MIN_PASSWORD_LENGTH = 8

def main():
	password = get_password()
	print_asterisks(password)


def print_asterisks(password):
	print('*' * len(password))


def get_password():
	password = input("Password: ")
	while len(password) < MIN_PASSWORD_LENGTH:
		print("Password doesn't meet a minimum length of 8 characters.")
		password = input("Password: ")
	return password


main()
