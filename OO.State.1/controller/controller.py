from controller.tipoFerramenta.ferramentalinha import FerramentaLinha
from controller.tipoFerramenta.ferramentarabisco import FerramentaRabisco
from controller.tipoFerramenta.ferramentacirculo import FerramentaCirculo
from controller.tipoFerramenta.ferramentaoval import FerramentaOval
from controller.tipoFerramenta.ferramentaretangulo import FerramentaRetangulo
from controller.tipoFerramenta.ferramentapoligono import FerramentaPoligono

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
        cor_borda = self.view.obter_cor_borda()
        cor_preenchimento = self.view.obter_cor_preenchimento()

        # cada ferramenta sabe dizer, por si mesma (polimorfismo, método
        # finalizada()), se já terminou seu trabalho; não precisa mais
        # checar aqui se o tipo é "Polígono"
        if self.ferramenta is None or self.ferramenta.finalizada():
            self.ferramenta = self.classes[tipo](self.desenho, self.view)

        self.ferramenta.mouse_pressionado(event, cor_borda, cor_preenchimento)

    def arraste_clicado(self, event):
        self.ferramenta.arraste_clicado(event)

    def solto(self, event):
        self.ferramenta.solto()

    def arraste(self, event):
        # não precisa mais checar isinstance(figura_nova, Poligono):
        # as ferramentas que não usam isso simplesmente não fazem nada
        if self.ferramenta is not None:
            self.ferramenta.arraste(event)

    def cliqueduplo(self, event):
        if self.ferramenta is not None:
            self.ferramenta.cliqueduplo()

    def salvar(self):
        caminho = self.view.escolher_arquivo_para_salvar()

        if not caminho:
            return

        # o controller só repassa o caminho do arquivo pro model; quem
        # sabe montar e escrever os dados é o próprio Desenho
        try:
            self.desenho.salvar(caminho)
        except OSError as erro:
            self.view.mostrar_erro("Erro ao salvar", str(erro))

    def abrir(self):
        caminho = self.view.escolher_arquivo_para_abrir()

        if not caminho:
            return

        try:
            self.desenho.abrir(caminho)
            self.ferramenta = None
            self.atualizar_tela()
        except (OSError, json.JSONDecodeError, KeyError, TypeError) as erro:
            self.view.mostrar_erro("Erro ao abrir", str(erro))

    def atualizar_tela(self):
        self.desenho.desenhar(self.view.canvas)