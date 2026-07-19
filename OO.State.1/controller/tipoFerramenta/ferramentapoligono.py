from controller.tipoFerramenta.ferramentadesenho import FerramentaDesenho

from model.tipoFigura.poligono import Poligono

class FerramentaPoligono(FerramentaDesenho):
    # ao contrário das outras ferramentas, o Polígono precisa de vários
    # cliques pra terminar uma única figura, então o construtor fica igual
    # ao das outras (desenho, view) e quem decide se é o primeiro clique
    # (começando um polígono novo) ou um clique seguinte (adicionando mais
    # um ponto) é o próprio mouse_pressionado, olhando se já existe uma
    # figura_nova em andamento
    def mouse_pressionado(self, event, corBorda, corFill):
        if self.desenho.figura_nova is None:
            coordenadas = [(event.x, event.y), (event.x, event.y)]
            pontos = [(event.x, event.y)]
            self.desenho.figura_nova = Poligono(coordenadas, pontos, corBorda, corFill=corFill)
        elif self.desenho.figura_nova.coordenadas[0] != (event.x, event.y):
            self.desenho.figura_nova.alterarPontosFinais(event.x, event.y)
            self.desenho.figura_nova.alterarPontosIniciais(event.x, event.y)
            self.desenho.figura_nova.adicionarPonto((event.x, event.y))
            self.desenho.desenhar(self.view.canvas)
            self.desenho.figura_nova.desenhar(self.view.canvas, tracejado=(4, 2))

    def arraste(self, event):
        if self.desenho.figura_nova is not None:
            self.desenho.figura_nova.alterarPontosFinais(event.x, event.y)
            self.desenho.desenhar(self.view.canvas)
            self.desenho.figura_nova.desenhar(self.view.canvas, tracejado=(4, 2))

    def cliqueduplo(self):
        if self.desenho.figura_nova is None:
            return

        if not self.desenho.figura_nova.incompleta():
            self.desenho.figura_nova.completo = True
            self.desenho.adicionar_figura(self.desenho.figura_nova)
            self.desenho.desenhar(self.view.canvas)
            self.desenho.figura_nova.desenhar(self.view.canvas)
            self.desenho.figura_nova = None
        else:
            self.desenho.figura_nova = None
            self.desenho.desenhar(self.view.canvas)

    def solto(self):
        pass

    def arraste_clicado(self, event):
        pass

    def finalizada(self):
        # enquanto houver uma figura_nova em andamento, o polígono ainda
        # não terminou e a mesma ferramenta deve continuar sendo usada
        return self.desenho.figura_nova is None