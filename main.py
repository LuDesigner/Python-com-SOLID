from cliente import Cliente
from item import Item
from pedido.pedido_retirada import PedidoRetirada
from pedido.pedido_delivery import PedidoDelivery

cliente = Cliente("Lais", "Alura")
item_um = Item("Pizza", 30.00)
item_dois = Item("Suco", 5.00)
itens = [item_um, item_dois]

taxa_entrega = 10.00

pedido_retirada = PedidoRetirada(cliente, itens)
pedido_delivery = PedidoDelivery(cliente, itens, taxa_entrega)

print(f"Preço do pedido Delivery: R$ {pedido_delivery.calcular_total():.2f}")
