#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
# As perguntas são: ""Telefonou para a vítima?"" ""Esteve no local do crime?"" ""Mora perto da vítima?""
# ""Devia para a vítima?"" ""Ját rabalhou com a vítima?""


#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como ""Suspeita"",
#entre 3 e 4 como ""Cúmplice""e 5 como ""Assassino"". Caso contrário,ele será classificado como ""Inocente"". 



perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]

respostas = []


for pergunta in perguntas:
    resposta = input(pergunta + " (sim ou não): ")
    respostas.append(resposta)


contador_respostas_positivas = 0
for resposta in respostas:
    if resposta == "sim":
        contador_respostas_positivas += 1


classificacao = None
if contador_respostas_positivas == 2:
    classificacao = "Suspeita"
elif contador_respostas_positivas >= 3 and contador_respostas_positivas <= 4:
    classificacao = "Cúmplice"
elif contador_respostas_positivas == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"


print("Classificação:", classificacao)

