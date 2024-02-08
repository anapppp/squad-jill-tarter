import json


class Cliente():
    def __init__(self, id, nome, telefone, endereco):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco

    def __str__(self):
        return json.dumps({
            "id": str(self.id),
            "nome": self.nome,
            "telefone": self.telefone,
            "endereco": self.endereco})
