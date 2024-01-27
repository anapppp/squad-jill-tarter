'''Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma
média de 5 calorias por minuto de exercício.'''

horas_exercicio = int(input('Quantas horas pratica exercício por semana?'))

#Cálculo das calorias
calorias_por_minuto = 5
semanas_mes = 4
minutos_exercicio = horas_exercicio*60
gasto_energetico_semana = minutos_exercicio*5
gasto_energetico_mes = gasto_energetico_semana*semanas_mes

print(f'O seu gasto calórico com exercícios mensalmente é: {gasto_energetico_mes} calorias.')