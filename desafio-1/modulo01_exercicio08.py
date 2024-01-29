'''Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês.Calcule e mostre o total do seu
salário no referido mês.'''

valor_hora = float(input('Informe o valor recebido pela hora trabalhada:'))
horas_trabalhadas = int(input('Informe a quantidade de horas trabalhadas mensalmente: '))

#Cálculo do salário
salario = valor_hora*horas_trabalhadas

print(f'O seu salário é R${salario:.2f}.')