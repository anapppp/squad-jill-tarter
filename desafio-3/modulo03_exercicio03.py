## Crie um dicionário representando um carrinho de compras. 
##Adicione produtos(chaves) equantidades(valores) ao carrinho. Calcule o total do carrinho de compra.


carrinho = {}

carrinho["maçã"] = 3
carrinho["banana"] = 2
carrinho["laranja"] = 1


total = 0
for produto, quantidade in carrinho.items():
    total += quantidade * produto

print("Total do carrinho:", total)