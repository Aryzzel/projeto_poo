from abc import ABC, abstractmethod
from math import dist


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


class Linha(Figura):
    def alterarPontosFinais(self, x, y):
        self.coordenadas[2], self.coordenadas[3] = x, y

    def desenhar(self, canvas, tracejado=None):
        x1, y1, x2, y2 = self.coordenadas
        canvas.create_line(x1, y1, x2, y2, fill=self.corBorda, dash=tracejado)

    def incompleta(self):
        return (self.coordenadas[0] == self.coordenadas[2]) and (self.coordenadas[1] == self.coordenadas[3])


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


class Circulo(Linha):
    def desenhar(self, canvas, tracejado=None):
        x1, y1, x2, y2 = self.coordenadas
        raio = dist((x1, y1), (x2, y2))
        canvas.create_oval(x1-raio, y1-raio, x1+raio, y1+raio, outline=self.corBorda, fill=self.corFill, dash=tracejado)


class Oval(Linha):
    def desenhar(self, canvas, tracejado=None):
        x1, y1, x2, y2 = self.coordenadas
        canvas.create_oval(x1, y1, x2, y2, outline=self.corBorda, fill=self.corFill, dash=tracejado)


class Retangulo(Linha):
    def desenhar(self, canvas, tracejado=None):
        x1, y1, x2, y2 = self.coordenadas
        canvas.create_rectangle(x1, y1, x2, y2, outline=self.corBorda, fill=self.corFill, dash=tracejado)


class Poligono(Figura):
    # vai ganhando pontos aos poucos, um a cada clique, até o usuário fechar a forma com dois cliques
    def __init__(self, pontos, corBorda, corFill=""):
        super().__init__(pontos, corBorda, corFill)
        self.pontos = self.coordenadas

    def adicionarPonto(self, novoPonto):
        self.pontos.append(novoPonto)

    def desenhar(self, canvas, tracejado=None):
        if len(self.pontos) >= 3:
            # create_polygon já fecha a forma sozinho (liga o último ponto no primeiro)
            canvas.create_polygon(self.pontos, outline=self.corBorda, fill=self.corFill, dash=tracejado)
        elif len(self.pontos) == 2:
            # com só 2 pontos ainda n dá pra preencher nada, mostra só a linha entre eles
            canvas.create_line(self.pontos, fill=self.corBorda, dash=tracejado)

    def incompleta(self):
        # precisa de pelo menos 3 pontos pra formar um polígono de verdade
        return len(self.pontos) < 3