numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

print(numero1)
print(numero2)

sum = numero1 + numero2

print("Suma", sum)

resta = numero1 - numero2
print("Resta", resta)

multiplicacion = numero1 * numero2
print("multiplicacion", multiplicacion)

division = numero1 / numero2
print ("division", division)

divisiondividendo = numero1 // numero2
print ("divisiondividendo", divisiondividendo)

divisionresto = numero1 % numero2
print("divisionresto", divisionresto)

potencia = numero1 ** numero2
print ("potencia", potencia)

celsius = float(input("Introduce los grados Celsius: "))

fahrenheit = celsius * 9 / 5 + 32

print("Fahrenheit:", fahrenheit)

eurosparadolares = 1.10

euros = float(input("Introduce una cantidad en euros: "))
dolares = euros * eurosparadolares
print (f"dolares: {dolares:.2f}")
