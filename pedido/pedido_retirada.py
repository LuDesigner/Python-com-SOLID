from pedido.pedido import Pedido

class PedidoRetirada(Pedido):
    def __init__(self, cliente, itens):
        super().__init__(cliente, itens)

    def calcular_total(self):
        return sum(item['preco'] * item['quantidade'] for item in self.itens)