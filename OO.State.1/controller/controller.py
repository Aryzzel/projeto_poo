from controller.tipoFerramenta.ferramentalinha import  FerramentaLinha
from controller.tipoFerramenta.ferramentarabisco import  FerramentaRabisco
from controller.tipoFerramenta.ferramentacirculo import  FerramentaCirculo
from controller.tipoFerramenta.ferramentaoval import  FerramentaOval
from controller.tipoFerramenta.ferramentaretangulo import  FerramentaRetangulo
from controller.tipoFerramenta.ferramentapoligono import FerramentaPoligono

from model.tipoFigura.poligono import Poligono


class Controller:
    def __init__(self, desenho, view):
        self.desenho = desenho
        self.view = view
        self.classes = {'Linha': FerramentaLinha,
                        'Rabisco': FerramentaRabisco,
                        'Círculo': FerramentaCirculo,
                         'Oval': FerramentaOval,
                         'Retângulo': FerramentaRetangulo,
                         'Polígono': FerramentaPoligono}

        self.ferramenta = None
        # Eventos de mouse associados ao canvas - com seus callbacks
        self.view.canvas.bind('<ButtonPress-1>', self.iniciar_figura)
        self.view.canvas.bind('<Motion>', self.arraste) # faz o polígoono seguir o mouse
        self.view.canvas.bind('<B1-Motion>', self.arraste_clicado)
        self.view.canvas.bind('<ButtonRelease-1>', self.solto)
        self.view.canvas.bind('<Double-Button-1>', self.cliqueduplo)  # duplo-clique fecha o polígono
        

    
    def iniciar_figura(self, event):
        tipo = self.view.obter_tipo_figura()
        x = event.x
        y = event.y
        cor_borda = self.view.obter_cor_borda()
        cor_preenchimento = self.view.obter_cor_preenchimento()


        if tipo == "Polígono":
            if not isinstance(self.desenho.figura_nova, Poligono):
                self.ferramenta = self.classes[tipo](self.desenho, self.view, event, cor_borda, cor_preenchimento)
        else:
            self.ferramenta = self.classes[tipo](self.desenho, self.view)
        
        self.mouse_pressionado(event, cor_borda, cor_preenchimento)
    
    def mouse_pressionado(self, event, corBorda, corFill):
        self.ferramenta.mouse_pressionado(event, corBorda, corFill)

    def arraste_clicado(self, event):
        self.ferramenta.arraste_clicado(event)
    
    def solto(self, event):
        self.ferramenta.solto()

    def arraste(self, event):
        if isinstance(self.desenho.figura_nova, Poligono):
            self.ferramenta.arraste(event)
        else:
            return
        
    def cliqueduplo(self, event):
        if isinstance(self.desenho.figura_nova, Poligono):
            self.ferramenta.cliqueduplo()
        else:
            return



