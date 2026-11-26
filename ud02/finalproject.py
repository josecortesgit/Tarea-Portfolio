USER = "admin"
PASSWORD = "asir2026"
MAX_TRIES = 3

logged_in = False


for attempt in range(1, MAX_TRIES + 1):
    user = input("User: ")
    pwd = input("Password: ")

    if user == USER and pwd == PASSWORD:
        print("Access granted")
        logged_in = True
        break
    else:
        print("Wrong credentials")
        print("Attempts left:", MAX_TRIES - attempt)
else:
    print("Account locked")



if logged_in:
    while True:
        print("\n== ADMIN CONSOLE ==")
        print("1) Port  2) Password  3) Backup  q) Quit")

        option = input("> ").strip().lower()

        match option:

            case "1":
                try:
                    port = int(input("Port: "))

                    if port < 0 or port > 65535:
                        print("Invalid port")
                    elif port <= 1023:
                        print(port, "is a WELL-KNOWN port")
                    elif port <= 49151:
                        print(port, "is a REGISTERED port")
                    else:
                        print(port, "is a DYNAMIC port")

                except ValueError:
                    print("Error: enter a valid number")

            
            case "2":
                password = input("Enter a password: ")

                has_digit = False
                has_upper = False

                for letter in password:
                    if letter.isdigit():
                        has_digit = True

                    if letter.isupper():
                        has_upper = True

                if len(password) >= 8 and has_digit and has_upper:
                    print("Strong password")
                else:
                    print("Weak password")

            case "3":
                try:
                    n = int(input("Countdown: "))

                    if n < 0:
                        print("Invalid number")
                    else:
                        for i in range(n, -1, -1):
                            print(i)

                        print("Backup started")

                except ValueError:
                    print("Error: enter a valid number")

            case "q":
                print("Goodbye!")
                break

            case _:
                print("Unknown option")
