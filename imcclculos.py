altura = input("Sua altura: ")
peso = input("Seu peso: ")
altura_int = int(altura)
peso_int = int(peso)
imc = peso_int / (altura_int ** 2)
print("IMC é de: ", imc)