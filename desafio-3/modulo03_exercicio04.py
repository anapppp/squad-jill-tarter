""" Crie um dicionário representando contatos (nome, telefone).
Permita ao usuário procurar por um contato pelo nome """

contatos = {}
contatos['bruno'] = '(11)99445-6672'
contatos['roberta'] = '(45)91719-1719'
contatos['alessandra'] = '(11)2002-1001'
contatos['caio'] = '(21)91898-1898'
contatos['yasmin'] = '(98)94002-8922'
contatos['eduarda'] = '(11)96663-6664'


nome = input('Digite o nome do contato que deseja buscar: ').lower()
if nome in contatos:
    print(f'O contato do(a) {nome} é: {contatos[nome]}')
else:
    print('O contato informado não está na lista!')