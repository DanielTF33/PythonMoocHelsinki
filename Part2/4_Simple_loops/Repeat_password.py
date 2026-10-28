while True:

    password = input("Password: ")
    repeat = input("Repeat password:")

    if  password == repeat:
        print("User account created!")
        break

    else:
        print("They do not match!")