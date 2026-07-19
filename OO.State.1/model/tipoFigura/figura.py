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

    def to_dict(self):
        """Converte a figura num dicionário pronto pra virar JSON.
        Subclasses com dados extras (Polígono) sobrescrevem e complementam."""
        return {
            "tipo": type(self).__name__,
            "coordenadas": self.coordenadas,
            "cor_borda": self.corBorda,
            "cor_preenchimento": self.corFill,
        }

    @classmethod
    def from_dict(cls, dados):
        """Reconstrói a figura a partir do dicionário lido do JSON.
        Subclasses com construtor diferente (Polígono) sobrescrevem."""
        return cls(dados["coordenadas"], dados["cor_borda"], dados["cor_preenchimento"])