## Faça um programa que lê três números inteiros e os mostra em ordem crescente

def ler_e_ordenar_numeros():

  
  numero1 = 0
  numero2 = 0
  numero3 = 0

 
  print("Digite o primeiro número: ")
  numero1 = int(input())

  print("Digite o segundo número: ")
  numero2 = int(input())

  print("Digite o terceiro número: ")
  numero3 = int(input())

  
  if numero1 > numero2:
    numero1, numero2 = numero2, numero1

  if numero1 > numero3:
    numero1, numero3 = numero3, numero1

  if numero2 > numero3:
    numero2, numero3 = numero3, numero2

 
  print("Os números em ordem crescente são:", numero1, ",", numero2, ",", numero3)


if __name__ == "__main__":
  ler_e_ordenar_numeros()