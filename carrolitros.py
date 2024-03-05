cidade = input("Digite o nome da cidade: ")
distancia = input("Distancia até a cidade: ")
gasolina_uso = input("Kilometros por litro: ")
preço = input("Preço da gasolina: ")
preço_int = int(preço)
gasolina_int = int(gasolina_uso)
distancia_int = int(distancia)
km_litro = gasolina_int / distancia_int
preço_viagem = preço_int * km_litro
print("Você está indo para: ",cidade)
print("A viagem vai custar: ",preço_viagem)
