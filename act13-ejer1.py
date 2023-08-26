# Pedir al usuario que ingrese un valor en grados fahrenheit
fahrenheit = input ("ingrese un valor en grados fahrenheit")

#convertir un valor a numero decimal
fahrenheit = float(fahrenheit)
# Aplicar la fórmula para obtener los grados Celsius
celsius = (fahrenheit - 32) * 5 / 9
#Mostrar en pantalla el resultado 
print (f"El valor en grados Celsius es: {celsius:.2f}")
print("\n")
# Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.

# Pedir al usuario que ingrese dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Calcular la suma, resta, división y multiplicación de los números
suma = num1 + num2
resta = num1 - num2
division = num1 / num2
multiplicacion = num1 * num2

# Mostrar los resultados en la pantalla
print("La suma de los números es:", suma)
print("La resta de los números es:", resta)
print("La división de los números es:", division)
print("La multiplicación de los números es:", multiplicacion)
print("\n")

# Calcular el perímetro y área de un rectángulo dada su base y su altura.

# Pedir al usuario que ingrese la base y la altura del rectángulo
base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

# Calcular el perímetro y el área del rectángulo
perimetro = 2 * (base + altura)
area = base * altura

# Mostrar los resultados en la pantalla
print("El perímetro del rectángulo es:", perimetro)
print("El área del rectángulo es:", area)