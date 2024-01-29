# Exercícios Banco de Dados

import sqlite3

conexao = sqlite3.connect('banco-desafio-2')
cursor = conexao.cursor()

# 1. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto). ok
# cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT,curso VARCHAR(100));')

# 2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior. OK
# cursor.execute("INSERT INTO alunos (id, nome, idade, curso) VALUES (1, 'Maria', 35, 'Banco de Dados'), (2, 'José', 45, 'Java Script'), (3, 'Renato', 24, 'Python'), (4, 'Giovane', 52, 'Banco de Dados'), (5, 'Andressa', 31, 'Java Scrip');")

# 3. Consultas Básicas
#   Escreva consultas SQL para realizar as seguintes tarefas:
#   a) Selecionar todos os registros da tabela "alunos".
# alunos = cursor.execute("SELECT * FROM alunos")
# for i in alunos:
#     print(i)

#   b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
# alunos = cursor.execute("SELECT nome, idade FROM alunos WHERE idade > 20")
# for i in alunos:
#     print(i)

#   c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
# alunos = cursor.execute("SELECT * FROM alunos WHERE curso LIKE 'Engenharia' ORDER BY nome")
# for i in alunos:
#     print(i)

#   d) Contar o número total de alunos na tabela
# alunos = cursor.execute("SELECT COUNT(*) FROM alunos;")
# for i in alunos:
#     print(i)

# 4. Atualização e Remoção
#   a) Atualize a idade de um aluno específico na tabela.
# cursor.execute("UPDATE alunos SET nome = 'Claudio' where id=4")

#   b) Remova um aluno pelo seu ID.
# cursor.execute("DELETE FROM alunos WHERE id=5")


# 5. Criar uma Tabela e Inserir Dados
# Crie uma tabela chamada "" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.

# cursor.execute( 'CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT,saldo FLOAT);')
# cursor.execute("INSERT INTO clientes (id, nome, idade, saldo) VALUES (1, 'Maria', 35, 456.02), (2, 'José', 45, 456.24), (3, 'Renato', 24, 45684.10 ), (4, 'Giovane', 52, 94.35), (5, 'Andressa', 31, 482.45);")

# 6. Consultas e Funções Agregadas
# Escreva consultas SQL para realizar as seguintes tarefas:
#   a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
# clientes = cursor.execute("SELECT nome, idade FROM clientes WHERE idade > 30")
# for i in clientes:
#     print(i)

#   b) Calcule o saldo médio dos clientes.
# clientes = cursor.execute("SELECT AVG(saldo) FROM clientes")
# for i in clientes:
#     print(i)

#   c) Encontre o cliente com o saldo máximo.
# clientes = cursor.execute("SELECT * FROM clientes where saldo = (SELECT MAX(saldo) FROM clientes);")
# for i in clientes:
#     print(i)

#   d) Conte quantos clientes têm saldo acima de 1000.
# clientes = cursor.execute("SELECT COUNT(*) FROM clientes WHERE saldo > 1000")
# for i in clientes:
#     print(i)

# 7. Atualização e Remoção com Condições
#   a) Atualize o saldo de um cliente específico.
# cursor.execute('UPDATE clientes SET saldo=1234.52 WHERE id=4;')

#   b) Remova um cliente pelo seu ID.
# cursor.execute('DELETE FROM clientes WHERE id=1;')

# 8. Junção de Tabelas
# Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real).
# cursor.execute('CREATE TABLE compras (id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor FLOAT, FOREIGN KEY (cliente_id) REFERENCES clientes(id));')

# Insira algumas compras associadas a clientes existentes na tabela "clientes".
# cursor.execute('INSERT INTO compras (id, cliente_id, produto, valor) VALUES (1, 5,"mouse",45.5 ), (2, 4,"teclado",31.99 ), (3, 4,"mouse", 45.5 ), (4, 2,"lampada", 9.99)')

# Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.
dados = cursor.execute(
    'SELECT clientes.nome, compras.produto, compras.valor FROM compras JOIN clientes ON compras.cliente_id = clientes.id')
for i in dados:
    print(i)

conexao.commit()
conexao.close()
