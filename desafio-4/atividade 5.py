def contar_vogais(frase):
    
    vogais = ["a", "e", "i", "o", "u","A" , "E", "I", "O", "U"]

    
    nVogais = 0

    
    for letra in frase:
        
        if letra in vogais:
            
            nVogais += 1

    return nVogais



frase = input("Insira uma frase: ")


numero_vogais = contar_vogais(frase)


print(f"A frase '{frase}' tem {numero_vogais} vogais.")