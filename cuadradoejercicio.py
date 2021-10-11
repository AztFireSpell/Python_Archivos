#Sacar solo el perimetro y area del cuadrado, usamos un try para evitar 
#error si no hay un numero

try:
    lado = int(input("Ingresa un lado del cuadrado:"))
except:
    print("no ha ingresado un numero!")
    
area = pow(lado, 2) #eleva al cuadrado
perimetro = lado * 4 # perimetro
print("El area del cuadrado es:",area,"cm2, y su perimetro es:", perimetro,"m")


