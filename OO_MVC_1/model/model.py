from figuras import Poligono


class Model:
    def __init__(self):
        self.figuras = []
        self.figura_nova = None

    def obter_figuras(self):
        return self.figuras

    def obter_figura_nova(self):
        return self.figura_nova

    def poligono_em_construcao(self):
        return isinstance(self.figura_nova, Poligono)