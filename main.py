from cliente import Cliente
from item import Item
from pedido.pedido_delivery import PedidoDelivery
from pagamento.pagamento_factory import PagamentoFactory
from notificacao.notificacao_facade import NotificacaoFacade
from observador.observador_status import ObservadorStatus

cliente = Cliente("Lais", "Alura")
item_um = Item("Pizza", 30.00)
item_dois = Item("Suco", 5.00)
itens = [item_um, item_dois]

taxa_entrega = 10.00

pedido = PedidoDelivery(cliente, itens, taxa_entrega)

valor_pedido = pedido.calcular_total()
tipo_pagamento = "pix"
pagamento = PagamentoFactory.criar_pagamento(tipo_pagamento).processar(valor_pedido)

MENSAGEM_PAGO = f"Pagamento de {valor_pedido} via {tipo_pagamento} realizado com sucesso!"
MENSAGEM_PREPARANDO = "Seu pedido está sendo preparado!"
MENSAGEM_ENVIADO = "Seu pedido saiu para entrega!"

notificacoes = NotificacaoFacade()
observador = ObservadorStatus(notificacoes)
pedido.adicionar_observadores(observador)

pedido.status = MENSAGEM_PAGO
pedido.status = MENSAGEM_PREPARANDO
pedido.status = MENSAGEM_ENVIADO