## Crie um programa que leia quanto dinheiro uma pessoa tem na carteira,e 
## calcule quanto poderia comprar de cada moeda estrangeira. Considere a tabela de conversão abaixo:
## Dólar maericano:R$4,91 
## Peso Argentino:R$0,02 
## Dólar Australiano:R$3,18 
## Dólar Canadense:R$3,64 
## Franco Suiço:R$0,42 E
## Euro:R$5,36 
## Libra esterlina:R$6,21

import math
moedas = {
    "dólar americano": 4.91, 
    "peso argentino": 0.02, 
    "dólar australiano": 3.18, 
    "dólar canadense": 3.64, 
    "franco suíço": 0.42, 
    "euro": 5.36, 
    "libra esterlina": 6.21 
}

reais = float(input("Quanto dinheiro você tem em reais na carteira? "))

for moeda in moedas: 
    quantidade_compra = reais / moedas[moeda]
    print(f"Com R${reais} você pode comprar {quantidade_compra:.2f} {moeda}.")
