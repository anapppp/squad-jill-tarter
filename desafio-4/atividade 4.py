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
