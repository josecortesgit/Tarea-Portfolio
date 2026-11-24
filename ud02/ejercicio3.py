
# 1. Cuenta atras

n = int(input("Enter a number: "))

while n >= 0:
    end = ", " if n > 0 else "\n"
    print(n, end=end)
    n -= 1


# 2. Suma y media

total = 0
count = 0

number = float(input("Enter a number (0 to stop): "))

while number != 0:
    total += number
    count += 1
    number = float(input("Enter a number (0 to stop): "))

print("Sum:", total)

if count > 0:
    average = total / count
    print("Average:", average)
else:
    print("No numbers entered")


# 3. Tabla de multiplicar

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# 4. Validacion

port = int(input("Enter a port (1-65535): "))

while port < 1 or port > 65535:
    print("Invalid port")
    port = int(input("Enter a port (1-65535): "))

print("Valid port:", port)
