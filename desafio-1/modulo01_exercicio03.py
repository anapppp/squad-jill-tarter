''' Faça um Programa que peça a quantidade de quilômetros,
transforme em metros, centímetros e milímetros
'''

print('O numero digitado estará em km')
km = float(input('Digite um numero, para tranformar em m, cm e mm: '))
primeira = km*1000
segunda =  km*100000
terceira = km*1000000

print(f'km-m: {primeira}, km-cm: {segunda}, km-mm: {terceira}')