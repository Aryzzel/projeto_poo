import json

from model.tipoFigura.linha import Linha
from model.tipoFigura.rabisco import Rabisco
from model.tipoFigura.circulo import Circulo
from model.tipoFigura.oval import Oval
from model.tipoFigura.retangulo import Retangulo
from model.tipoFigura.poligono import Poligono


class Desenho:
    # mapeia o nome do tipo (salvo no JSON) pra classe correspondente,
    # assim reabrir um arquivo não precisa de um if/elif pra cada tipo:
    # quem sabe reconstruir a figura é a própria classe (Figura.from_dict)
    TIPOS_FIGURA = {
        'Linha': Linha,
        'Rabisco': Rabisco,
        'Circulo': Circulo,
        'Oval': Oval,
        'Retangulo': Retangulo,
        'Poligono': Poligono,
    }

    def __init__(self):
        self.figuras = []
        self.figura_nova = None

    def desenhar(self, canvas):
        canvas.delete('all')
        for item in self.figuras:
            item.desenhar(canvas)

    def adicionar_figura(self, figura):
        self.figuras.append(figura)

    def obter_figuras(self):
        return self.figuras

    def obter_figura_nova(self):
        return self.figura_nova

    def salvar(self, caminho):
        """Salva o desenho atual no arquivo indicado. Quem monta os dados
        de cada figura é a própria figura (polimorfismo via to_dict)."""
        dados = [figura.to_dict() for figura in self.figuras]

        with open(caminho, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    def abrir(self, caminho):
        """Carrega um desenho salvo em disco, substituindo o atual.
        Erros (arquivo inválido, tipo desconhecido, etc.) sobem pra quem
        chamou tratar - o model só sabe ler e montar as figuras."""
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)

        self.figuras = [
            self.TIPOS_FIGURA[dado['tipo']].from_dict(dado)
            for dado in dados
        ]
        self.figura_nova = None