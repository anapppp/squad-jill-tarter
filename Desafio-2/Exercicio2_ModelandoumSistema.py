# O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres. 
# Modele um sistema orientado a objetos para representar contas correntes do Banco Delas seguindo os requisitos abaixo.
# Cada conta corrente pode ter um ou mais clientes como titular.
# O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
# A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.
# Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela fizer um depósito, aumentaremos o saldo.
# Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda mensal, ou seja, elas
# podem sacar valores que deixam a sua conta com valor negativo até renda_mensal.
# Clientes homens por enquanto não têm direito a cheque especial.
#Para modelar seu sistema, utilize obrigatoriamente os conceitos
#"classe", "herança", "propriedades", "encapsulamento" e "classe abstrata".

from abc import ABC, abstractmethod
class BaseCliente(ABC):
    def __init__(self, nome, telefone, renda_mensal):
        self.nome = nome
        self.telefone = telefone
        self.renda_mensal = renda_mensal

    @abstractmethod
    def cheque_especial(self):
        pass


class ClienteM(BaseCliente):
    def __init__(self, nome, telefone, renda_mensal):
        super().__init__(nome, telefone, renda_mensal)

    def cheque_especial(self):
        return True


class ClienteH(BaseCliente):
    def __init__(self, nome, telefone, renda_mensal):
        super().__init__(nome, telefone, renda_mensal)

    def cheque_especial(self):
        return False


class ContaCorrente:
    def __init__(self, clientes):
        self.clientes = clientes
        self.saldo = 0
        self.operacoes = []

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(f"Depósito de R${valor:.2f} realizado")
        print('DEPÓSITO REALIZADO!')

    def saque(self, valor):
        if self.tem_saldo_suficiente(valor):
            self.saldo -= valor
            self.operacoes.append(f"Saque de R${valor:.2f} realizado")
            print("SAQUE REALIZADO!")




cliente_m = ClienteM("Paula", "911223344", 20000)
cliente_h = ClienteH("Paulo", "955667788", 700)

conta_paula = ContaCorrente([cliente_m])
conta_paulo = ContaCorrente([cliente_h])



