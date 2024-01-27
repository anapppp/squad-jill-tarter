## Faça um Programa que peça dois números e imprima o maior deles.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if numero1 > numero2:
    maiorNumero = numero1
else:
    maiorNumero = numero2

print("O maior número é:", maiorNumero)