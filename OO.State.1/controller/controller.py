from controller.tipoFerramenta.ferramentalinha import  FerramentaLinha
from controller.tipoFerramenta.ferramentarabisco import  FerramentaRabisco
from controller.tipoFerramenta.ferramentacirculo import  FerramentaCirculo
from controller.tipoFerramenta.ferramentaoval import  FerramentaOval
from controller.tipoFerramenta.ferramentaretangulo import  FerramentaRetangulo
from controller.tipoFerramenta.ferramentapoligono import FerramentaPoligono

from model.tipoFigura.poligono import Poligono
from model.tipoFigura.linha import Linha
from model.tipoFigura.rabisco import Rabisco
from model.tipoFigura.circulo import Circulo
from model.tipoFigura.oval import Oval
from model.tipoFigura.retangulo import Retangulo

import json

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

        self.view.botao_salvar.config(command=self.salvar)
        self.view.botao_abrir.config(command=self.abrir)
        

    
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

    def salvar(self):
        caminho = self.view.escolher_arquivo_para_salvar()

        if not caminho:
            return

        dados = [
            self.converter_figura_para_dados(figura)
            for figura in self.desenho.figuras
        ]

        try:
            with open(caminho, "w", encoding="utf-8") as arquivo:
                json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        except OSError as erro:
            self.view.mostrar_erro("Erro ao salvar", str(erro))

    def abrir(self):
        caminho = self.view.escolher_arquivo_para_abrir()

        if not caminho:
            return

        try:
            with open(caminho, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

            self.desenho.figuras = [
                self.converter_dados_para_figura(dado)
                for dado in dados
            ]
            self.desenho.figura_nova = None
            self.ferramenta = None
            self.atualizar_tela()

        except (OSError, json.JSONDecodeError, KeyError, TypeError) as erro:
            self.view.mostrar_erro("Erro ao abrir", str(erro))

    def converter_figura_para_dados(self, figura):
        dados = {
            "tipo": type(figura).__name__,
            "coordenadas": figura.coordenadas,
            "cor_borda": figura.corBorda,
            "cor_preenchimento": figura.corFill
        }

        if isinstance(figura, Rabisco):
            dados["pontos"] = figura.pontos

        if isinstance(figura, Poligono):
            dados["pontos"] = figura.pontos
            dados["completo"] = figura.completo

        return dados

    def converter_dados_para_figura(self, dados):
        tipo = dados["tipo"]
        coordenadas = dados["coordenadas"]
        cor_borda = dados["cor_borda"]
        cor_preenchimento = dados["cor_preenchimento"]

        if tipo == "Linha":
            return Linha(coordenadas, cor_borda, cor_preenchimento)

        if tipo == "Rabisco":
            return Rabisco(dados["pontos"], cor_borda, cor_preenchimento)

        if tipo == "Circulo":
            return Circulo(coordenadas, cor_borda, cor_preenchimento)

        if tipo == "Oval":
            return Oval(coordenadas, cor_borda, cor_preenchimento)

        if tipo == "Retangulo":
            return Retangulo(coordenadas, cor_borda, cor_preenchimento)

        if tipo == "Poligono":
            return Poligono(
                coordenadas,
                dados["pontos"],
                cor_borda,
                dados["completo"],
                cor_preenchimento
            )

        raise KeyError("Tipo de figura inválido")

    def atualizar_tela(self):
        self.desenho.desenhar(self.view.canvas)