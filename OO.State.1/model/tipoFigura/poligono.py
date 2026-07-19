from model.tipoFigura.figura import Figura

class Poligono(Figura):
    # vai ganhando pontos aos poucos, um a cada clique, até o usuário fechar a forma com dois cliques
    def __init__(self, coordenadas, pontos, corBorda, completo=False, corFill=""):
        super().__init__(coordenadas, corBorda, corFill)
        self.completo = completo
        self.pontos = pontos

    def adicionarPonto(self, novoPonto):
        self.pontos.append(novoPonto)

    def alterarPontosFinais(self, x, y):
        self.coordenadas[1] =  (x, y)

    def alterarPontosIniciais(self, x, y):
        self.coordenadas[0] = (x, y)

    def desenhar(self, canvas, tracejado=None):
        if self.completo == False:
            canvas.create_line(self.coordenadas, fill=self.corBorda, dash=tracejado)
        if len(self.pontos) > 1:
            canvas.create_line(self.pontos, fill=self.corBorda, dash=tracejado)
        if len(self.pontos) >= 3 and self.completo==True:
            # create_polygon já fecha a forma sozinho (liga o último ponto no primeiro)
            canvas.create_polygon(self.pontos, outline=self.corBorda, fill=self.corFill, dash=tracejado)

    def incompleta(self):
        # precisa de pelo menos 3 pontos pra formar um polígono de verdade
        return len(self.pontos) < 3

    def to_dict(self):
        dados = super().to_dict()
        dados["pontos"] = self.pontos
        dados["completo"] = self.completo
        return dados

    @classmethod
    def from_dict(cls, dados):
        return cls(
            dados["coordenadas"],
            dados["pontos"],
            dados["cor_borda"],
            dados["completo"],
            dados["cor_preenchimento"],
        )