## Reverso do número.Faça uma função que retorne o reverso de um número inteiro informado.
## Por exemplo:127->721.

def reverso(numero):
    string_numero = str(numero)
    reverso = ""
    for unidade in string_numero:
        reverso = unidade + reverso
    print(reverso)

numero = 127
reverso(numero)
