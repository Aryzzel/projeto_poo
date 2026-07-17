from .figuras import Linha, Rabisco, Circulo, Oval, Retangulo, Poligono


class Model:
    def __init__(self):
        self.figuras = []
        self.figura_nova = None

    def iniciar_figura(self, tipo, x, y, cor_borda, cor_preenchimento=""):
        if tipo == "Polígono":
            if isinstance(self.figura_nova, Poligono):
                self.figura_nova.adicionarPonto((x, y))
                self.figura_nova.coordenadas[0] = (x, y)
                self.figura_nova.coordenadas[1] = (x, y)
            else:
                self.figura_nova = Poligono(
                    [(x, y), (x, y)],
                    [(x, y)],
                    cor_borda,
                    corFill=cor_preenchimento
                )
            return

        if tipo == "Linha":
            self.figura_nova = Linha([x, y, x, y], cor_borda, cor_preenchimento)
        elif tipo == "Rabisco":
            self.figura_nova = Rabisco([(x, y)], cor_borda, cor_preenchimento)
        elif tipo == "Círculo":
            self.figura_nova = Circulo([x, y, x, y], cor_borda, cor_preenchimento)
        elif tipo == "Oval":
            self.figura_nova = Oval([x, y, x, y], cor_borda, cor_preenchimento)
        elif tipo == "Retângulo":
            self.figura_nova = Retangulo([x, y, x, y], cor_borda, cor_preenchimento)

    def atualizar_figura(self, x, y):
        if self.figura_nova is None:
            return

        if isinstance(self.figura_nova, Rabisco):
            self.figura_nova.adicionarPonto((x, y))
        else:
            self.figura_nova.alterarPontosFinais(x, y)

    def finalizar_figura(self):
        if self.figura_nova is None or isinstance(self.figura_nova, Poligono):
            return

        if not self.figura_nova.incompleta():
            self.figuras.append(self.figura_nova)

        self.figura_nova = None

    def finalizar_poligono(self):
        if not isinstance(self.figura_nova, Poligono):
            return

        if not self.figura_nova.incompleta():
            self.figura_nova.completo = True
            self.figuras.append(self.figura_nova)

        self.figura_nova = None

    def obter_figuras(self):
        return self.figuras

    def obter_figura_nova(self):
        return self.figura_nova

    def poligono_em_construcao(self):
        return isinstance(self.figura_nova, Poligono)