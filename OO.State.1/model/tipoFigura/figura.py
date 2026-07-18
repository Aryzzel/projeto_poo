from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, coordenadas, corBorda, corFill=""):
        self.coordenadas = coordenadas
        self.corBorda = corBorda
        self.corFill = corFill

    @abstractmethod
    def desenhar(self, canvas, tracejado=None):
        pass

    @abstractmethod
    def incompleta(self):
        pass
