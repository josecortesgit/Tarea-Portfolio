try:
    number = int(input("Integer: "))
    print("You entered:", number)
except ValueError:
    print("That is not a valid number")
