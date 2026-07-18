from model.tipoFigura.figura import Figura

class Linha(Figura):
    def alterarPontosFinais(self, x, y):
        self.coordenadas[2], self.coordenadas[3] = x, y

    def desenhar(self, canvas, tracejado=None):
        x1, y1, x2, y2 = self.coordenadas
        canvas.create_line(x1, y1, x2, y2, fill=self.corBorda, dash=tracejado)

    def incompleta(self):
        return (self.coordenadas[0] == self.coordenadas[2]) and (self.coordenadas[1] == self.coordenadas[3])