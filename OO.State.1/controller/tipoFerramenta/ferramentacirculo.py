from controller.tipoFerramenta.ferramentadesenho import FerramentaDesenho
from controller.tipoFerramenta.ferramentalinha import FerramentaLinha

from model.tipoFigura.circulo import Circulo

class FerramentaCirculo(FerramentaDesenho):
    def mouse_pressionado(self, event, corBorda, corFill):
        FerramentaLinha.mouse_pressionado(self, event, corBorda, corFill)
        self.desenho.figura_nova = Circulo(self.coordenadas, self.corBorda, self.corFill)
    
    def arraste_clicado(self, event):
        FerramentaLinha.arraste_clicado(self, event)
    
    def solto(self):
        FerramentaLinha.solto(self)