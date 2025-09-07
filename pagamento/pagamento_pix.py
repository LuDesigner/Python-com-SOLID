from pagamento.pagamento import Pagamento

class PagamentoPIX(Pagamento):
    def processar(self, valor):
        print(f"Processando pagamento no PIX no valor de R$ {valor:.2f}")