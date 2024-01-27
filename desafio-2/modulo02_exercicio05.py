## Desenvolva um programa que solicite ao usuário os comprimentos do strês lados de um triângulo e 
## classifique-o como equilátero, isósceles ou escaleno. 
## 3equilátero: todos os lados com o mesmo valor.
## isósceles:dois lados com o mesmo valor 
## escaleno: todos os lados com medidas distintas.

lado1 = float(input('Primeiro lado: '))
lado2 = float(input('Segundo  lado: '))
lado3 = float(input('Terceiro lado: '))

if (lado1 + lado2 < lado3) or (lado1 + lado3 < lado3) or (lado2 + lado3 < lado1):
        print('Nao é um triangulo')
elif (lado1 == lado2) and (lado1 == lado2) :
        print('Equilatero')
elif (lado1==lado2) or (lado1==lado3) or (lado2==lado3):
        print('Isósceles')
else:
        print('Escaleno')