from app.models.produto import Produto

class Produto:
    def __init__(self, nome, categoria, marca, preco, quantidade, fornecedor):
        self.nome = nome
        self.categoria = categoria
        self.marca = marca
        self.preco = preco
        self.quantidade = quantidade
        self.fornecedor = fornecedor
        
produto = Produto("Ração Premium", "Ração", "PetNutri", 89.90, 20, "Distribuidora Pet")

print(f"Produto: {produto.nome}")
print(f"Categoria: {produto.categoria}")
print(f"Marca: {produto.marca}")
print(f"Preço: R${produto.preco:.2f}")
print(f"Quantidade: {produto.quantidade}")
print(f"Fornecedor: {produto.fornecedor}")