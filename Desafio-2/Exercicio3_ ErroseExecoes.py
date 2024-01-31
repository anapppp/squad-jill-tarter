## O programa abaixo deve calcular a média dos valores digitados pelo usuário.
## No entanto, ele não está funcionando bem. Você pode consertá-lo?

##o erro se encontra no calculo da média, pois o indice da lista pode nçao ser 1 número.
## também alterei a media para aceitar valores decimais (float) 
## criada a condição de número válido ou inválido

def calcular_media(valores):
    tamanho = len(valores)
    soma = 0.0
    for valor in valores:
        soma += valor
    media = soma / float(tamanho)
    return media

continuar = True
valores = []
while continuar:
    valor = input('Digite um número para entrar na sua média ou "calcular" para calcular o valor:')
    if valor.lower() == 'calcular':
        continuar = False
    if not valor.isdigit():
        print('O valor digitado não é um número.')
        continue
    valores.append(float(valor))

media = calcular_media(valores)
print('A média calculada para os valores {} foi de {}'.format(valores, media))