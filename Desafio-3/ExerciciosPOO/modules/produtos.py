import json


class Produto():
    def __init__(self, id, nome, qtd_estoque):
        self.id = id
        self.nome = nome
        self.qtd_estoque = int(qtd_estoque)

    def __str__(self):
        return json.dumps({
            "id": str(self.id),
            "nome": self.nome,
            "qtd_estoque": str(self.qtd_estoque)
        })

    def comprar(self, quantidade):
        if quantidade > self.qtd_estoque:
            print(
                f"A quantidade do produto {self.nome} em estoque é insuficiente")
        else:
            self.qtd_estoque -= quantidade


# Class Fornecedor
