## Crie um programa que solicite ao usuário um login e uma senha. 
## O programa deve permitir o acesso a penas se ousuário for "admin"e a senha for "admin123",
## caso contrário imprima uma mensagem de erro.

login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

if login == "admin" and senha == "admin123":
    print("Login efetuado com sucesso")
else:
    print("Login inválido")