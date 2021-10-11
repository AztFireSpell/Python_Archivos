#Este ejercicio va calculando los montos hasta que se ingrese un 0
#si el monto total es mayor a 150000 se aplica un descuento

#para esperar un resultado, si llega el resultado cambia la ejecucion

bandera = 1

#bandera sea 1 quiere decir que el monto es mayor a 0

montototal = 0

#mientras no se cumpla algo entonces ejecuta
while(bandera != 0):
    monto = int(input("Ingresa el monto del cliente:"))    
    #monto sea mayor a 0 porque si es menor representa un numero 
    #negativo
    
    if(monto < 0):
        print("El monto no es valido, intente de nuevo")
    else:
        montototal = montototal + monto
        
        if(monto == 0):
            bandera = 0
            
            if(montototal > 150000):
                print("!!Descuento aplicable por valor de monto mayor a 150000 --")
                print("Cantidad sin descuento:", montototal)
                montototal = (15 * montototal / 100)
                print("El monto total a pagar con descuento es de:", montototal)
                print("Cantidad de dinero descontada:", (montototal * .15))
                
                
                
            else:
                print("El monto total a pagar es de:", montototal)
    
    