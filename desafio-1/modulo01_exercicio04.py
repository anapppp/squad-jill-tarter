## Receba do usuário a quantidade de litros de combustível consumidos e a distancia percorrida.
## Calcule e imprima o consumo médio em km-l.

km = int(input("Digite quantos km você rodou: "))
l= int(input("Digite quantos litros de combustível você gastou: "))

consumo= km/l

print(f'O seu carro tem o consumo médio de {consumo:.2f} km/l.')