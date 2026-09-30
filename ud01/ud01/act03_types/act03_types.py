# act03_types.py
integer_number = 5
decimal_number = 3.14
text = "Hola esto es texto"
is_student = True
empty_value = None

print(f"{integer_number} -> {type(integer_number)}")
print(f"{decimal_number} -> {type(decimal_number)}")
print(f"{text} -> {type(text)}")
print(f"{is_student} -> {type(is_student)}")
print(f"{empty_value} -> {type(empty_value)}")
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
#“Python, comprueba si 0.1 + 0.2 es exactamente igual a 0.3 y dime si es verdadero o falso”.
#0.1 + 0.2 no da exactamente 0.3 porque los números float se guardan en el ordenador como 
#aproximaciones binarias. Por eso el resultado real es 0.30000000000000004 y la comparación con 0.3 devuelve False.
print("3" + 3)
#El error aparece porque "3" es un texto (str) y 3 es un número entero (int). Python no puede sumarlos directamente porque son tipos de datos diferentes.
