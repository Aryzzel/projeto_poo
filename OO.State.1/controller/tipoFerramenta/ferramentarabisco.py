from controller.tipoFerramenta.ferramentadesenho import FerramentaDesenho
from controller.tipoFerramenta.ferramentalinha import FerramentaLinha

from model.tipoFigura.rabisco import Rabisco

class FerramentaRabisco(FerramentaDesenho):
    def mouse_pressionado(self, event, corBorda, corFill):
        self.corBorda = corBorda
        self.corFill = corFill
        self.pontos = [(event.x, event.y)]

        self.desenho.figura_nova = Rabisco(self.pontos, self.corBorda, self.corFill)
    
    def arraste_clicado(self, event):
        self.desenho.figura_nova.adicionarPonto((event.x, event.y))
        self.desenho.desenhar(self.view.canvas)
        self.desenho.figura_nova.desenhar(self.view.canvas, tracejado=(4,2))

    def solto(self):
        FerramentaLinha.solto(self)    