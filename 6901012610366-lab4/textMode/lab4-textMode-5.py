import getpass
user_password = getpass.getpass("Enter your password: ")
if user_password == "1234":
    print("Access granted")
else:
    print("Access denied")
