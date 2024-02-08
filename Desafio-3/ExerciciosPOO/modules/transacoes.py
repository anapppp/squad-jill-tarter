# 5. O mercado mantém um registro de todas as transações
# realizadas, incluindo detalhes como data da compra, cliente
# envolvido e quantidade de produtos comprados.
from datetime import datetime
from json import dumps
from modules.clientes import Cliente


class Compra():
    def __init__(self, id, cliente, lista_compras, data=None):
        self.id = id
        self.data = data if data else datetime.now()
        self.cliente = cliente if isinstance(
            cliente, Cliente) else print("Cliente inválido")
        self.lista_compras = lista_compras

    def __str__(self):
        return dumps({
            "id": str(self.id),
            "cliente_nome": str(self.cliente.nome),
            "compras": [
                {"produto": str(i[0].nome),
                 "quantidade": str(i[1])}
                for i in self.lista_compras]
        })
