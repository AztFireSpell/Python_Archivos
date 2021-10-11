#Ejercicio en donde calculamos el area del triangulo escaleno

from math import sqrt
#nos trae operaciones para las matematicas
#sqrt = raiz cuadrada

lado1 = int(input("Ingresa el primer lado de tu triangulo escaleno!"))
lado2 = int(input("Ingresa el primer lado de tu triangulo escaleno!"))
lado3 = int(input("Ingresa el primer lado de tu triangulo escaleno!"))

s = ((lado1 + lado2 +lado3)/2)

area = sqrt(s *((s - lado1) * (s - lado2) * (s - lado3)))

print("El area del triangulo es:", area)
print("El perimetro del triangulo es:", (lado1 + lado2 + lado3))