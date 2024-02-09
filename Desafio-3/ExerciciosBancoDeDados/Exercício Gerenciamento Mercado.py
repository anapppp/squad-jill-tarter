import sqlite3
conexao = sqlite3.connect('mercado')
cursor = conexao.cursor()

# tabela clientes
cursor.execute ("CREATE TABLE Clientes (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nome VARCHAR (150), cpf VARCHAR (11), endereco TEXT, telefone VARCHAR(15))")

# inserindo na tabela clientes 
comando_sql = "INSERT INTO Clientes (nome, cpf, endereco, telefone) VALUES (?,?,?,?)"

valores = [
    ("Ana Lucia", 46983222768, "Rua Tres Lagos n15, Canindé, São Paulo/SP", 987633544),
    ("Vera Maria", 78441333861, "Rua Pedro Alto n20, Vl Gumercindo, São Paulo/SP", 9638774199),
    ("Pedro Felipe", 736810944688, "Rua Tres Lagos n9, Canindé, São Paulo/SP", 37964888),
    ("Matheus Silva", 36971428501, "Travessa Alfenins s/n, Arroi, São Paulo/SP", 369771566),
    ("Arthur Aguias", 10223888948, "Rua Domm Pedro n8, Canindé, São Paulo/SP", 327896633),
]

cursor.executemany(comando_sql, valores)

# tabela produtos
cursor.execute("CREATE TABLE Produtos (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nome VARCHAR(150), preco DECIMAL(10,2), descricao TEXT, categoria VARCHAR (150), quantidade_estoque INT, fornecedor_id INT, FOREIGN KEY (fornecedor_id) REFERENCES Fornecedores(id))")

# inserindo na tabela produtos
comando_sql = "INSERT INTO Produtos (nome, preco, descricao, categoria, quantidade_estoque, fornecedor_id) VALUES (?,?,?,?,?,?)"

valores = [
    ("Coca Cola", 7.50, "Refrigerante sabor cola 2L", "Bebidas", 10, 1),
    ("Banana", 9.60, "Banana nanica kg", "Hortifruti", 15, 2),
    ("Detergente", 4.50, "Lava louça neutro", "Limpeza", 4, 3),
    ("Manga", 2.10, "Manga palmer un", "Hortifruti", 18, 2),
    ("Candida", 15.00, "Água sanitária com cloro ativo 2L", "Limpeza", 10, 3),
]

cursor.executemany(comando_sql, valores)


# tabela fornecedores
cursor.execute("CREATE TABLE Fornecedores (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nome VARCHAR(150), cnpj VARCHAR (14), telefone VARCHAR (15))")

# Inserindo Fornecedores
comando_sql = "INSERT INTO Fornecedores (nome, cnpj, telefone) VALUES (?,?,?)"

valores = [
    ("Bebidas Brasil", 96327146000176, 11-987664399),
    ("Dois Irmaos Horti Fruti", 36327146000141, 11-978663488),
    ("Higienizas", 87467146000136, 11-37466822),
]

cursor.executemany(comando_sql, valores)


# tabela vendas
cursor.execute("CREATE TABLE Vendas (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, data DATE, cliente_id INT, produto_id INT, quantidade_compra INT, forma_de_pagamento INT, FOREIGN KEY (cliente_id) REFERENCES Clientes(id), FOREIGN KEY (produto_id) REFERENCES Produtos(id))")

# Inserindo vendas
comando_sql = "INSERT INTO Vendas (data, cliente_id, produto_id, quantidade_compra, forma_de_pagamento) VALUES (?, ?, ?, ?,?)"

valores = [
   ("2023-11-14", 1, 2, 1,"débito"),
    ("2023-11-15", 2, 3, 2,"crédito"),
    ("2023-11-16", 3, 1, 3, "dinheiro"),
    ("2023-11-17", 1, 4, 1, "crédito"),
    ("2023-11-18", 2, 2, 2, "dinheiro"),
]

cursor.executemany(comando_sql, valores)

# tabela produto e fornecedores
cursor.execute("CREATE TABLE Produtos_fornecedores( id_relacionamento INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,produto_id INT, fornecedor_id INT, FOREIGN KEY (produto_id) REFERENCES Produtos(id), FOREIGN KEY (fornecedor_id) REFERENCES Fornecedores(id))")

# Inserindo Produtos_fornecedores individualmente para teste
dados = cursor.execute ('INSERT INTO Produtos_fornecedores (produto_id, fornecedor_id) VALUES (5,3)')


# Questão 3: 
#Listar produtos em estoque
dados = cursor.execute('SELECT * FROM Produtos WHERE quantidade_estoque > 0')
for produto in dados:
    print(produto)

#Encontrar as vendas realizadas por um cliente específico
dados = cursor.execute('SELECT * FROM Vendas WHERE cliente_id = 1')
for Vendas in dados:
  print(Vendas)  

#Calcular o total de vendas por categoria de produto:
dados = cursor.execute('SELECT Produtos.categoria, SUM(Produtos.preco * Vendas.quantidade_compra) AS totalVendas FROM Produtos JOIN Vendas ON Produtos.id = Vendas.produto_id GROUP BY Produtos.categoria ')
for totalVendas in dados:
  print(totalVendas)   

#Identificar os produtos mais vendidos:
dados = cursor.execute('SELECT Produtos.nome, SUM(Vendas.quantidade_compra) AS total_vendas FROM Produtos JOIN Vendas ON Produtos.id = Vendas.produto_id GROUP BY Produtos.nome ORDER BY total_vendas DESC')
for total_vendas in dados:
   print(total_vendas) 

# Atualizar a quantidade em estoque do produto
dados = cursor.execute("UPDATE Produtos SET quantidade_estoque = quantidade_estoque - 1 WHERE id = 2")
for produto in dados:
   print(produto) 

# Atualizar o telefone de um cliente
dados = cursor.execute('UPDATE Clientes SET telefone = "39815150" WHERE id = 4')

# Excluir o cliente da tabela Clientes
cursor.execute("DELETE FROM Clientes WHERE id=2")
dados_clientes = cursor.execute("SELECT * FROM Clientes")
print("Cliente removido com sucesso:")
for cliente in dados_clientes:
    print(cliente)


# Fecha a conexão
conexao.commit()
cursor.close()
conexao.close()