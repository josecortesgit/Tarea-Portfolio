mark = float(input("Mark (0-10): "))

if mark < 0 or mark > 10:
    print("Invalid mark")
elif mark < 5:
    print("Fail / Insuficiente")
elif mark < 7:
    print("Pass / Aprobado")
elif mark < 9:
    print("Very good / Notable")
else:
    print("Excellent / Sobresaliente")

# Parte 2: Años bisiestos
year = int(input("Year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
