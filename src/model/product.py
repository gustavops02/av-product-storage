class Product:

    def __init__(self, codigo, nome, preco):
        TAXA = 0.1
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.precoAjustado = preco + (preco * TAXA)

    def __init__():
        pass