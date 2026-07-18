from model.tipoFigura.figura import Figura
from model.tipoFigura.linha import Linha

class Retangulo(Figura):
    def desenhar(self, canvas, tracejado=None):
        x1, y1, x2, y2 = self.coordenadas
        canvas.create_rectangle(x1, y1, x2, y2, outline=self.corBorda, fill=self.corFill, dash=tracejado)

    def alterarPontosFinais(self, x, y):
        Linha.alterarPontosFinais(self, x, y)
    
    def incompleta(self):
        return Linha.incompleta(self)