## Implemente um programa que classifique um aluno com base em sua pontuação em um exame.
## O programa deverá solicitar uma nota de 0 a 10.Se a pontuação for maior ou igual a7, 
## o aluno é aprovado; caso contrário, é reprovado.

nota = input("Digite sua nota de 0 a 10: ").upper()
if nota >= "7":
    print("Parabéns, você foi aprovado!")
elif nota < "N":
    print("Que pena, você foi reprovado!")
else:
    print("!")