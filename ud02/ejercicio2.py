print("1) Disk  2) Users  3) Ping  q) Quit")

option = input("> ").strip().lower()

match option:
    case "1":
        used = int(input("Used %: "))

        if used < 0 or used > 100:
            print("Invalid percentage")
        elif used > 90:
            print("CRITICAL")
        elif used > 80:
            print("WARNING")
        else:
            print("Disk OK")

    case "2":
        print("Users: admin, user1, user2")

    case "3":
        ip = input("Enter IP: ")

        if len(ip.split(".")) == 4:
            print("Simulated ping to", ip)
        else:
            print("Invalid IP")

    case "q":
        print("Goodbye!")

    case _:
        print("Unknown option")

