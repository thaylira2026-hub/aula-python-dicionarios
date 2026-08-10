produtos = []

def cadastrar_produto(codigo, descricao, quantidade, preco):
    produto = {
        "codigo": codigo,
        "descricao": descricao,
        "quantidade": quantidade,
        "preco": preco
    }
    produtos.append(produto)


def listar_produtos():
    for produto in produtos:
        print(produto)


def buscar_produto(codigo):
    for produto in produtos:
        if produto["codigo"] == codigo:
            return produto
    return None


def remover_produto(codigo):
    produto = buscar_produto(codigo)
    if produto:
        produtos.remove(produto)
        return True
    return False



cadastrar_produto(123, "camiseta branca", 100, 85.00)
cadastrar_produto(124, "calça jeans", 50, 150.00)

listar_produtos()
