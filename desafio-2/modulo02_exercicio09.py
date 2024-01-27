## O programa deve calcular e apresentar a quantidade de números parese ímpares inseridos.
## O processo de leitura deve ser encerrado quando o usuário informar o valor zero. 
## Certifique-sede incluir validações para garantir que apenas números positivos sejam considerados
## na contagem e cálculos.

def main():
    numeros_pares = 0
    numeros_impares = 0

    
    while True:
        numero = int(input("Informe um número: "))

       
        if numero < 0:
            print("Número inválido. Digite um número positivo.")
            continue

        
        if numero % 2 == 0:
            numeros_pares += 1
        else:
            numeros_impares += 1

    
        if numero == 0:
            break

  
    print("Quantidade de números pares:", numeros_pares)
    print("Quantidade de números ímpares:", numeros_impares)


if __name__ == "__main__":
    main()