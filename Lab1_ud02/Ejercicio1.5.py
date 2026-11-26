try:
    mark = float(input("Mark (0-10): "))

except ValueError:
    print("Invalid mark: enter a number")

else:
    if not 0 <= mark <= 10:
        print("Invalid mark")
    elif mark < 5:
        print("Fail")
    elif mark < 7:
        print("Pass")
    elif mark < 9:
        print("Very good")
    else:
        print("Excellent")
