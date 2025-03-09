password = input("Enter password: ")

if len(password) >=6 and "#"in password and password[0].isupper():
    print("Sicher")
else:
    print("Unsicher")

