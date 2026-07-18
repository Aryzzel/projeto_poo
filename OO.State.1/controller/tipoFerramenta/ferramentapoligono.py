from controller.tipoFerramenta.ferramentadesenho import FerramentaDesenho

from model.tipoFigura.poligono import Poligono

class FerramentaPoligono(FerramentaDesenho):
    def __init__(self, desenho, view, event, corBorda, corFill):
        super().__init__(desenho, view)
        
        self.coordenadas = [(event.x, event.y), (event.x, event.y)]
        self.pontos = [(event.x, event.y)]
        self.corBorda = corBorda
        self.corFill = corFill
        self.desenho.figura_nova = Poligono(self.coordenadas, self.pontos, self.corBorda, corFill=self.corFill)

    def mouse_pressionado(self, event, corBorda, corFill):
        if self.desenho.figura_nova.coordenadas[0] != (event.x, event.y):
            self.desenho.figura_nova.alterarPontosFinais(event.x, event.y)
            self.desenho.figura_nova.alterarPontosIniciais(event.x, event.y)
            self.desenho.figura_nova.adicionarPonto((event.x, event.y))
            self.desenho.desenhar(self.view.canvas)
            self.desenho.figura_nova.desenhar(self.view.canvas, tracejado=(4,2))


    def arraste(self, event):
        self.desenho.figura_nova.alterarPontosFinais(event.x, event.y)
        self.desenho.desenhar(self.view.canvas)
        self.desenho.figura_nova.desenhar(self.view.canvas, tracejado=(4,2))

    def cliqueduplo(self):
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