from model.tipoFigura.figura import Figura
from model.tipoFigura.linha import Linha

from math import dist

class Circulo(Figura):
    def desenhar(self, canvas, tracejado=None):
        x1, y1, x2, y2 = self.coordenadas
        raio = dist((x1, y1), (x2, y2))
        canvas.create_oval(x1-raio, y1-raio, x1+raio, y1+raio, outline=self.corBorda, fill=self.corFill, dash=tracejado)
    def alterarPontosFinais(self, x, y):
        Linha.alterarPontosFinais(self, x, y)
    
    def incompleta(self):
        return Linha.incompleta(self)