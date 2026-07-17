from abc import ABC, abstractmethod
from model.figuras import Linha, Rabisco, Circulo, Oval, Retangulo, Poligono

class FerramentaDesenho(ABC):
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    @abstractmethod
    def mouse_pressionado(self):
        pass

    @abstractmethod
    def arraste_clicado(self):
        pass

    @abstractmethod
    def solto(self):
        pass

class FerramentaLinha(FerramentaDesenho):
    def mouse_pressionado(self, event, corBorda, corFill): 
        self.corBorda = corBorda
        self.corFill = corFill
        self.coordenadas = [event.x, event.y, event.x, event.y]

        self.model.figura_nova = Linha(self.coordenadas, self.corBorda, self.corFill)

    def arraste_clicado(self, event):
        self.model.figura_nova.alterarPontosFinais(event.x, event.y)
        self.model.desenhar(self.view.canvas)
        self.model.figura_nova.desenhar(self.view.canvas, tracejado=(4,2))
        

    def solto(self):
        if not self.model.figura_nova.incompleta():
            self.model.adicionar_figura(self.model.figura_nova)
            self.model.desenhar(self.view.canvas)
            self.model.figura_nova = None
    

class FerramentaRabisco(FerramentaDesenho):
    def mouse_pressionado(self, event, corBorda, corFill):
        self.corBorda = corBorda
        self.corFill = corFill
        self.pontos = [(event.x, event.y)]

        self.model.figura_nova = Rabisco(self.pontos, self.corBorda, self.corFill)
    
    def arraste_clicado(self, event):
        self.model.figura_nova.adicionarPonto((event.x, event.y))
        self.model.desenhar(self.view.canvas)
        self.model.figura_nova.desenhar(self.view.canvas, tracejado=(4,2))

    def solto(self):
        FerramentaLinha.solto(self)    

class FerramentaCirculo(FerramentaDesenho):
    def mouse_pressionado(self, event, corBorda, corFill):
        FerramentaLinha.mouse_pressionado(self, event, corBorda, corFill)
        self.model.figura_nova = Circulo(self.coordenadas, self.corBorda, self.corFill)
    
    def arraste_clicado(self, event):
        FerramentaLinha.arraste_clicado(self, event)
    
    def solto(self):
        FerramentaLinha.solto(self)

class FerramentaOval(FerramentaDesenho):
    def mouse_pressionado(self, event, corBorda, corFill):
        FerramentaLinha.mouse_pressionado(self, event, corBorda, corFill)
        self.model.figura_nova = Oval(self.coordenadas, self.corBorda, self.corFill)
    
    def arraste_clicado(self, event):
        FerramentaLinha.arraste_clicado(self, event)
    
    def solto(self):
        FerramentaLinha.solto(self)

class FerramentaRetangulo(FerramentaDesenho):
    def mouse_pressionado(self, event, corBorda, corFill):
        FerramentaLinha.mouse_pressionado(self, event, corBorda, corFill)
        self.model.figura_nova = Retangulo(self.coordenadas, self.corBorda, self.corFill)
    
    def arraste_clicado(self, event):
        FerramentaLinha.arraste_clicado(self, event)
    
    def solto(self):
        FerramentaLinha.solto(self)

class FerramentaPoligono(FerramentaDesenho):
    def __init__(self, model, view, event, corBorda, corFill):
        super().__init__(model, view)
        
        self.coordenadas = [(event.x, event.y), (event.x, event.y)]
        self.pontos = [(event.x, event.y)]
        self.corBorda = corBorda
        self.corFill = corFill
        self.model.figura_nova = Poligono(self.coordenadas, self.pontos, self.corBorda, corFill=self.corFill)

    def mouse_pressionado(self, event, corBorda, corFill):
        if self.model.figura_nova.coordenadas[0] != (event.x, event.y):
            self.model.figura_nova.alterarPontosFinais(event.x, event.y)
            self.model.figura_nova.alterarPontosIniciais(event.x, event.y)
            self.model.figura_nova.adicionarPonto((event.x, event.y))
            self.model.desenhar(self.view.canvas)
            self.model.figura_nova.desenhar(self.view.canvas, tracejado=(4,2))


    def arraste(self, event):
        self.model.figura_nova.alterarPontosFinais(event.x, event.y)
        self.model.desenhar(self.view.canvas)
        self.model.figura_nova.desenhar(self.view.canvas, tracejado=(4,2))

    def cliqueduplo(self):
        if not self.model.figura_nova.incompleta():
            self.model.figura_nova.completo = True
            self.model.adicionar_figura(self.model.figura_nova)
            self.model.desenhar(self.view.canvas)
            self.model.figura_nova.desenhar(self.view.canvas)
            self.model.figura_nova = None
        else:
            self.model.figura_nova = None
            self.model.desenhar(self.view.canvas)

    def solto(self):
        pass
    def arraste_clicado(self, event):
        pass


    