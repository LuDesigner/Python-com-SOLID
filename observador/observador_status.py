class ObservadorStatus:
    def __init__(self, notificacao):
        self.notificacao = notificacao

    def atualizar(self, pedido):
        mensagem = f"O pedido foi atualização: {status}"
        self.notificacao.enviar_notificacao(pedido.cliente, mensagem)