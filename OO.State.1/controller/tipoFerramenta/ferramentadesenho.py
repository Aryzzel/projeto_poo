from abc import ABC, abstractmethod

class FerramentaDesenho(ABC):
    def __init__(self, desenho, view):
        self.desenho = desenho
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



    