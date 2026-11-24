
#Lee una altura y dibuja un triángulo rectángulo de asteriscos

height = int(input("Enter height: "))

for i in range(1, height + 1):
    for j in range(i):
        print("*", end="")
    print()


#Dibuja el mismo triángulo invertido

for i in range(height, 0, -1):
    for j in range(i):
        print("*", end="")
    print()


#Muestra la tabla de multiplicar completa 1-10 alineada con f-strings

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end="")
    print()


#Ampliación: un cuadrado hueco de lado n

n = int(input("Enter square size: "))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
