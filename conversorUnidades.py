#Un simple conversor de unidades de millas a km, m, ft, e in

millas = int(input("Ingresa cuantas millas quieres convertir:"))


print("La longitud en kilometros es:", (millas * 1.609344), "km")
print("La longitud en metros es:",(millas * 1609.344) ,"m")
print("La longitud en pies es:", (millas * 5280), "ft")
print("La longitud en pulgadas es:", (millas * 63360), "in")