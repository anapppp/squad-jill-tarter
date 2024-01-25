#Pergunta
distancia=int(input("Digite aqui qual é a distância, em km, da sua viagem: "))

#Avião
tempoaviao=(distancia/600)*60

#Carro
tempocarro= (distancia/100)*60

#Ônibus
tempoonibus=(distancia/80)*60

#Resposta
print(f"Se sua viagem for de avião você demorará {tempoaviao:.2f} m. Já de carro, demorará {tempocarro:.2f}m e de ônibus {tempoonibus:.2f}m.")
