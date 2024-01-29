'''Solicite ao usuário o peso em kg e a altura em metros. Calcule e
imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso / (altura x altura).'''

peso = float(input('Informe o seu peso em kg:'))
altura = float(input('Informe a sua altura em metros:'))

#Cálculo do IMC
imc = peso/(altura*altura)

print(f'O seu IMC é {imc:.2f}.')