from model.tipoFigura.figura import Figura

class Rabisco(Figura):
    def __init__(self, pontos, corBorda, corFill=""):
        super().__init__(pontos, corBorda, corFill)
        self.pontos = self.coordenadas

    def desenhar(self, canvas, tracejado=None):
        if len(self.pontos) > 1:
            canvas.create_line(self.pontos, fill=self.corBorda, dash=tracejado)

    def adicionarPonto(self, novoPonto):
        self.pontos.append(novoPonto)

    def incompleta(self):
        return len(self.pontos) <= 1