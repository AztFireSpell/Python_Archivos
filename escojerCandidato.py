#Dependiendo de la letra que ingrese el usuario este votara por un partido


print("Bienvenido, por favor escoja su candidato!\na.-Candidato A\nb.-Candidato B\nc.-Candidato C:")
candidato = (input("Ingrese la opcion de candidato:"))

#si se cumple algo ejecuta algo
#entonces si no se cumple ejecuta algo mas

if(candidato == 'a'):
    print("Usted a votado por el partido rojo!")
if(candidato == 'b'):
    print("Usted a votado por el partido verde!")
if(candidato == 'c'):
    print("Usted a votado por el partido azul!")
    
    # == !=
if((candidato != 'a') and (candidato != 'b') and (candidato != 'c')):
    print("Ha seleccionado opcion incorrecta")
                
        
    