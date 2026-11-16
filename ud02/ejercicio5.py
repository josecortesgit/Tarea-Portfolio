USER, PASSWORD = "admin", "asir2026"
MAX_TRIES = 3

attempt = 0

while attempt < MAX_TRIES:
    user = input("User: ")
    pwd = input("Password: ")

    if user == "" or pwd == "":
        print("Empty input. Try again.")
        continue

    attempt += 1

    if user == USER and pwd == PASSWORD:
        print("Access granted")
        break
    else:
        print("Wrong credentials")
        print("Attempts left:", MAX_TRIES - attempt)

else:
    print("Account locked")
