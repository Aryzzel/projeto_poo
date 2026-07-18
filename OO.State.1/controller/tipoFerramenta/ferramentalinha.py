from controller.tipoFerramenta.ferramentadesenho import FerramentaDesenho

from model.tipoFigura.linha import Linha

class FerramentaLinha(FerramentaDesenho):
    def mouse_pressionado(self, event, corBorda, corFill): 
        self.corBorda = corBorda
        self.corFill = corFill
        self.coordenadas = [event.x, event.y, event.x, event.y]

        self.desenho.figura_nova = Linha(self.coordenadas, self.corBorda, self.corFill)

    def arraste_clicado(self, event):
        if not self.desenho.figura_nova == None:
            self.desenho.figura_nova.alterarPontosFinais(event.x, event.y)
            self.desenho.desenhar(self.view.canvas)
            self.desenho.figura_nova.desenhar(self.view.canvas, tracejado=(4,2))
        

    def solto(self):
        if not self.desenho.figura_nova == None:
            if not self.desenho.figura_nova.incompleta():
                self.desenho.adicionar_figura(self.desenho.figura_nova)
                self.desenho.desenhar(self.view.canvas)
                self.desenho.figura_nova = None