from abc import ABC, abstractmethod

class Pedido(ABC):
    def __init__(self, cliente, itens):
        self.cliente = cliente
        self.itens = itens
        self._status = "Criado!"
        self.observadores = []

    @status.setter
    def status(self, novo_status):
        self._status = novo_status
        self.notificar_observadores

    def adicionar_observador(self, observador):
        self.observadores.append(observador)

    def notificar_observadores(self):
        for observador in self.observadores:
            observador.atualizar(self)

    @property
    def status(self):
        return self._status

    @abstractmethod
    def calcular_total(self):
        pass
