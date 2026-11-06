print("1) Disk 2) Users 3) Ping q) Quit")
option = input("> ").strip().lower()

match option:
    case "1":
        used = int(input("Used %: "))
        if used > 90:
            print("CRITICAL")
        elif used > 80:
            print("WARNING")
        else:
            print("OK")
    case "2":
        print("Show users: admin, guest")
    case "3":
        ip = input("IP: ")
        parts = ip.split(".")
        if len(parts) != 4:
            print("Invalid IP format")
        else:
            print(f"Pinging {ip}...")
    case "q":
        print("Bye!")
    case _:
        print("Unknown option")
