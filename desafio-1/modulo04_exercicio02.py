def reverso(numero):
    string_numero = str(numero)
    reverso = ""
    for unidade in string_numero:
        reverso = unidade + reverso
    print(reverso)

numero = 127
reverso(numero)
