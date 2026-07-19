from abc import ABC, abstractmethod

class FerramentaDesenho(ABC):
    def __init__(self, desenho, view):
        self.desenho = desenho
        self.view = view

        # declarados aqui pra não nascerem "escondidos" dentro de
        # mouse_pressionado (nas subclasses que usam); ferramentas que não
        # precisam de algum desses (ex: Polígono) simplesmente deixam None
        self.coordenadas = None
        self.pontos = None
        self.corBorda = None
        self.corFill = None

    @abstractmethod
    def mouse_pressionado(self, event, corBorda, corFill):
        pass

    @abstractmethod
    def arraste_clicado(self, event):
        pass

    @abstractmethod
    def solto(self):
        pass

    def arraste(self, event):
        # a maioria das ferramentas não faz nada enquanto o mouse só se move
        # (sem estar clicado); só o Polígono sobrescreve isso
        pass

    def cliqueduplo(self):
        # só o Polígono usa duplo-clique pra fechar a forma
        pass

    def finalizada(self):
        # indica se a ferramenta já terminou seu trabalho e o controller
        # deve criar uma nova no próximo clique. Só o Polígono, que precisa
        # de vários cliques pra terminar uma figura, sobrescreve isso
        return True