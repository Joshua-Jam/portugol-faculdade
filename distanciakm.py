km1 = input("Primeiro kilometro: ")
km2 = input("Segundo kilometro: ")
km1_int = int(km1)
km2_int = int(km2)
if km1_int < km2_int:
    kmdiferente = km2_int - km1_int
else:
    kmdiferente = km1_int + km2_int

print("A distancia entre os kilometros é: ", kmdiferente)