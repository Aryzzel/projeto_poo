from tkinter import *
from tkinter import ttk
from tkinter import colorchooser  # pra abrir aquela paleta de cores nativa do tkinter
from abc import ABC, abstractmethod
from math import dist


class Figura(ABC):
    def __init__(self, coordenadas, corBorda, corFill=""):
        self.coordenadas = coordenadas
        self.corBorda = corBorda
        self.corFill = corFill

    @abstractmethod
    def desenhar(self, canvas, tracejado=None):
        pass

    @abstractmethod
    def incompleta(self):
        pass


class Linha(Figura):
    def alterarPontosFinais(self, x, y):
        self.coordenadas[2], self.coordenadas[3] = x, y

    def desenhar(self, canvas, tracejado=None):
        x1, y1, x2, y2 = self.coordenadas
        canvas.create_line(x1, y1, x2, y2, fill=self.corBorda, dash=tracejado)

    def incompleta(self):
        return (self.coordenadas[0] == self.coordenadas[2]) and (self.coordenadas[1] == self.coordenadas[3])


class Rabisco(Figura):
    def __init__(self, pontos, corBorda, corFill=""):
        super().__init__(pontos, corBorda, corFill)
        self.pontos = self.coordenadas

    def desenhar(self, canvas, tracejado=None):
        if len(self.pontos) > 1:
            canvas.create_line(self.pontos, fill=self.corBorda, dash=tracejado)

    def adicionarPonto(self, novoPonto):
        self.pontos.append(novoPonto)

    def incompleta(self):
        return len(self.pontos) <= 1


class Circulo(Linha):
    def desenhar(self, canvas, tracejado=None):
        x1, y1, x2, y2 = self.coordenadas
        raio = dist((x1, y1), (x2, y2))
        canvas.create_oval(x1-raio, y1-raio, x1+raio, y1+raio, outline=self.corBorda, fill=self.corFill, dash=tracejado)


class Oval(Linha):
    def desenhar(self, canvas, tracejado=None):
        x1, y1, x2, y2 = self.coordenadas
        canvas.create_oval(x1, y1, x2, y2, outline=self.corBorda, fill=self.corFill, dash=tracejado)


class Retangulo(Linha):
    def desenhar(self, canvas, tracejado=None):
        x1, y1, x2, y2 = self.coordenadas
        canvas.create_rectangle(x1, y1, x2, y2, outline=self.corBorda, fill=self.corFill, dash=tracejado)


class AplicacaoDesenho:
    def __init__(self, root):
        self.root = root
        self.figuras = []  # Todas as figuras desenhadas
        self.figura_nova = None  # Figura que está sendo desenhada, mas ainda não foi incluída em figuras
        self.criar_interface()

    # Quando mouse é pressionado
    def iniciar_figura_nova(self, event):
        cor = self.cor_borda_atual.get()  # pega a cor que tá selecionada no momento do clique
        cor_p = self.cor_preenchimento_atual.get()

        if self.tipo_figura_var.get() == 'Linha':
            self.figura_nova = Linha([event.x, event.y, event.x, event.y], cor, cor_p)
        elif self.tipo_figura_var.get() == 'Rabisco':
            self.figura_nova = Rabisco([(event.x, event.y)], cor, cor_p)
        elif self.tipo_figura_var.get() == 'Círculo':
            self.figura_nova = Circulo([event.x, event.y, event.x, event.y], cor, cor_p)
        elif self.tipo_figura_var.get() == 'Oval':
            self.figura_nova = Oval([event.x, event.y, event.x, event.y], cor, cor_p)
        elif self.tipo_figura_var.get() == 'Retângulo':
            self.figura_nova = Retangulo([event.x, event.y, event.x, event.y], cor, cor_p)

    # Quando mouse é movido com o botão pressionado
    def atualizar_figura_nova(self, event):
        if self.figura_nova is None:
            return

        if isinstance(self.figura_nova, Rabisco):
            self.figura_nova.adicionarPonto((event.x, event.y))
        else:
            self.figura_nova.alterarPontosFinais(event.x, event.y)
        self.desenhar_figuras()
        self.desenhar_figura_nova()

    # Quando mouse é solto
    def incluir_figura_nova(self, event):
        # cor não é usada aqui, só serve pra desempacotar certo
        if self.figura_nova is not None and not self.figura_nova.incompleta():  # para evitar incluir figuras incompletas, como uma linha sem comprimento ou um rabisco com um único ponto
            self.figuras.append(self.figura_nova)
        self.figura_nova = None
        self.desenhar_figuras()

    def desenhar_figuras(self):
        self.canvas.delete("all")
        # cada figura agora vem com uma cor junto, por isso o for desempacota 3 valores e não mais 2
        for figura in self.figuras:
            figura.desenhar(self.canvas)

    def desenhar_figura_nova(self):
        if self.figura_nova is not None:
            self.figura_nova.desenhar(self.canvas, tracejado=(4, 2))

    # abre o seletor de cor e atualiza tanto a variável quanto a cor de fundo do botão, pra dar um feedback visual de qual cor tá selecionada
    def escolher_cor_borda(self):
        cor = colorchooser.askcolor(title="Escolha a cor da borda", initialcolor=self.cor_borda_atual.get())
        # cor é uma tupla tipo ((r,g,b), '#hexadecimal'), só interessa o hexadecimal
        if cor[1] is not None:  # se a pessoa clicar em cancelar, cor[1] vem None, então não faz nada
            self.cor_borda_atual.set(cor[1])
            self.botao_cor_borda.config(bg=cor[1])

    def escolher_cor_preenchimento(self):
        cor_inicial = self.cor_preenchimento_atual.get()
        cor_inicial = "#8c8488"
        cor = colorchooser.askcolor(title="Escolha a cor de preenchimento", initialcolor=cor_inicial)
        if cor[1] is not None:
            self.cor_preenchimento_atual.set(cor[1])
            self.botao_cor_preenchimento.config(bg=cor[1], fg="black")

    def remover_preenchimento(self):
        self.cor_preenchimento_atual.set("")
        self.botao_cor_preenchimento.config(bg="SystemButtonFace", fg="black")

    def criar_interface(self):
        self.frame = Frame(self.root)

        # Widgets arranjados com Layout grid dentro de frame
        paddings = {'padx': 5, 'pady': 5}

        # label
        label = ttk.Label(self.frame, text='Linha ou Rabisco:')
        label.grid(column=0, row=0, sticky=W, **paddings)

        # option menu
        self.tipo_figura_var = StringVar(self.root)  # Guarda o tipo de figura selecionado no option menu (linha ou rabisco)
        option_menu = ttk.OptionMenu(self.frame, self.tipo_figura_var,
                                     'Linha', 'Linha', 'Rabisco', 'Círculo', 'Oval', 'Retângulo')
        option_menu.grid(column=1, row=0, sticky=W, **paddings)

        # bordas com cor
        self.cor_borda_atual = StringVar(self.root,
                                         value='#000000')  # guarda a cor escolhida em hexadecimal ('#ff0000'), começa preto igual o padrão do tkinter
        self.botao_cor_borda = Button(self.frame, text='Cor da Borda', command=self.escolher_cor_borda,
                                      # botao que abre a paleta de cores; o bg dele serve de "preview" mostrando a cor atual
                                      bg=self.cor_borda_atual.get())
        self.botao_cor_borda.grid(column=2, row=0, sticky=W, **paddings)

        self.cor_preenchimento_atual = StringVar(self.root, value="")
        self.botao_cor_preenchimento = Button(self.frame, text='Preenchimento', command=self.escolher_cor_preenchimento)
        self.botao_cor_preenchimento.grid(column=3, row=0, sticky=W, **paddings)

        self.botao_sem_preenchimento = Button(self.frame, text='Transparente', command=self.remover_preenchimento)
        self.botao_sem_preenchimento.grid(column=3, row=1, sticky=W, **paddings)

        # Área de desenho
        self.canvas = Canvas(self.frame, bg='white', width=600, height=600)
        self.canvas.grid(column=0, row=2, columnspan=5, sticky=W, **paddings)

        self.frame.pack()

        # Eventos de mouse associados ao canvas - com seus callbacks
        self.canvas.bind('<ButtonPress-1>', self.iniciar_figura_nova)
        self.canvas.bind('<B1-Motion>', self.atualizar_figura_nova)
        self.canvas.bind('<ButtonRelease-1>', self.incluir_figura_nova)


# ******* MAIN *******#

root = Tk()
aplicacao = AplicacaoDesenho(root)
root.mainloop()