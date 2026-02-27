from abc import ABC, abstractmethod

# Interface do Produto
class Transporte(ABC):
    @abstractmethod
    def entregar(self):
        pass

# Produtos Concretos
class Caminhao(Transporte):
    def entregar(self):
        return "Entrega feita por terra em caixa blindada."

class Navio(Transporte):
    def entregar(self):
        return "Entrega feita por mar em container."

# Classe Criadora (A Fábrica)
class Logistica(ABC):
    @abstractmethod
    def criar_transporte(self):
        pass

    def organizar_entrega(self):
        transporte = self.criar_transporte()
        return f"Logística diz: {transporte.entregar()}"

# Fábricas Concretas
class LogisticaTerrestre(Logistica):
    def criar_transporte(self):
        return Caminhao()

class LogisticaMaritima(Logistica):
    def criar_transporte(self):
        return Navio()

# Uso do código
if __name__ == "__main__":
    entrega_terra = LogisticaTerrestre()
    print(entrega_terra.organizar_entrega())

    entrega_mar = LogisticaMaritima()
    print(entrega_mar.organizar_entrega())
