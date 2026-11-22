for number in range(1, 51):
    if number > 20 and number % 17 == 0:
        break
    if number % 3 == 0:
        continue
    print(number)
