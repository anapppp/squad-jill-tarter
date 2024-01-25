def conversao_celsius_fahrenheit():
        cf = (temperatura * (9/5)) + 32
        print(cf)

def conversao_fahrenheit_celsius():
        fc = (temperatura - 32) * (5/9)
        print(fc)

temperatura_usuario = input("Digite uma temperatura: ")
temperatura = float(temperatura_usuario)
escolha_metodo_conversao = input("Digite CF se você deseja converter a temperatura de celsius para fahrenheit OU FC se você deseja converter fahrenheit para celsius: ")

if escolha_metodo_conversao == "CF":
    conversao_celsius_fahrenheit()
else:
    conversao_fahrenheit_celsius()

