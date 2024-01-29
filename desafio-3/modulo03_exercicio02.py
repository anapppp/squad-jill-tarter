## Faça um Programa que peça as quatro notas de 5 alunos, calcule e armazene numa lista a média de cada aluno,
##2 imprima o número de alunos com média maior oui gual a 7.0.

medias = []

for aluno in range(5):

    notas = []
    for nota in range(4):
        nota = float(input("Digite a nota {} do aluno {}: ".format(nota + 1, aluno + 1)))
        notas.append(nota)


    media = sum(notas) / len(notas)


    medias.append(media)


contador_alunos_aprovados = 0
for media in medias:
    if media >= 7.0:
        contador_alunos_aprovados += 1

print("Número de alunos aprovados:", contador_alunos_aprovados)