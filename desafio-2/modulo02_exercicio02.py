##Faça um Programa que pergunte em que turno você estuda.
##Peça para digitar M-matutino ou V-Vespertino ou N-Noturno.
## Imprima a mensagem"Bom Dia!","BoaTarde!"ou"BoaNoite!"ou"ValorInválido!",conforme ocaso.

turno = input("Em qual turno você estuda? Digite M para Matutino, V para Vespertino ou N para Noturno: ")

if turno.upper() == 'M':
    mensagem = "Bom Dia!"
elif turno.upper() == 'V':
    mensagem = "Boa Tarde!"
elif turno.upper() == 'N':
    mensagem = "Boa Noite!"
else:
    mensagem = "Valor Inválido!"

print(mensagem)