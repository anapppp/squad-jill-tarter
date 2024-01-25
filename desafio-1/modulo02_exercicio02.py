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