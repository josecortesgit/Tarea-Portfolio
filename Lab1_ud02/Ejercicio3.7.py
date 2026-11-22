smallest = None
largest = None

while True:
    text = input("Integer (end to finish): ")
    if text == "end":
        break

    try:
        number = int(text)
    except ValueError:
        print("Warning: invalid integer ignored")
        continue

    if smallest is None or number < smallest:
        smallest = number
    if largest is None or number > largest:
        largest = number

if smallest is None:
    print("No numbers entered")
else:
    print("Largest:", largest)
    print("Smallest:", smallest)
