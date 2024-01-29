## Criar um programa em Python que solicite três números ao usuário,utilize estruturas
## condicionais para determinar o maior entre eles e apresente o resultado.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

maior =n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3


print(f"O maior número digitado foi {maior}")