''' Faça um Programa que peça dois números,
realize as principais operações soma,subtração,
multiplicação,divisão '''


numero1 = float(input('Digite o número 01: '))
numero2 = float(input('Digite o número 02: '))

soma = numero1+numero2
subtracao = numero1-numero2
multiplicacao = numero1*numero2
divisao = numero1/numero2

print(f'soma: {soma:.2f}, subtracao: {subtracao:.2f}, multiplicacao: {multiplicacao:.2f}, divisão: {divisao:.2f}')