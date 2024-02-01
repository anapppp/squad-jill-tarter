# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.
# Crie uma instância da classe carro.
# Faça o carro "andar" utilizando os métodos da sua classe.
#. Faça o carro "parar" utilizando os métodos da sua classe.

class Carro:
    def __init__(self, cor, modelo):
        self.ligado = False
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0

    def liga(self):
        if not self.ligado:
            self.ligado = True
            print(f"O carro {self.modelo} está ligado.")
       

    def desliga(self):
        if self.ligado:
            
            self.velocidade = 0
            print(f"O carro {self.modelo} está desligado.")
       

    def andar(self,velocidade):
        if self.ligado:
            self.velocidade = velocidade
            print(f"O carro {self.modelo} está andando a {self.velocidade} km/h.")
            

    def parar(self):
        if self.velocidade != 0:
            print(f"O carro {self.modelo} parou.")
           
    
# Criando uma instância da classe Carro
carro1= Carro(cor="vermelho", modelo="Spin")

# Fazendo o carro andar
carro1.liga()
carro1.andar(60)

# Parando o carro
carro1.parar()
