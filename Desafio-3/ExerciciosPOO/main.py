"""
Gerenciamento de Mercado:

Vamos criar um sistema orientado a objetos para representar um
sistema de mercado seguindo os requisitos fornecidos:

1. Cada produto pode ter um ou mais fornecedores.
2. O mercado controla apenas o nome, o telefone e o endereço de
cada cliente.
3. Cada produto tem um nome, uma lista de categorias às quais
pertence e uma quantidade disponível em estoque.
4. Quando um produto é comprado, sua quantidade disponível em
estoque é reduzida.
5. O mercado mantém um registro de todas as transações
realizadas, incluindo detalhes como data da compra, cliente
envolvido e quantidade de produtos comprados.
"""


# Criar classes
# Usar Casse, Herança, Propriedades, encapsulamento e classe abstrata
from uuid import uuid4
from modules import clientes, produtos, transacoes

# Cliente
novo_cliente = clientes.Cliente(
    id=uuid4(),
    nome="Maria",
    telefone="123456",
    endereco="Rua das margaridas")

# Fornecedor
novo_fornecedor = produtos.Fornecedor(
    id=uuid4(),
    nome="Granja Bananal"
)

# Produto
banana = produtos.Produto(
    id=uuid4(),
    nome="Banana",
    qtd_estoque="100")

maca = produtos.Produto(
    id=uuid4(),
    nome="Maçã",
    qtd_estoque="150")

banana.adicionar_fornecedor(novo_fornecedor)
maca.adicionar_fornecedor(novo_fornecedor)

# Transacao
lista_de_compras = [(banana, 20), (maca, 10)]

nova_transacao = transacoes.Compra(
    id=uuid4(), cliente=novo_cliente, lista_compras=lista_de_compras)

print(nova_transacao)
