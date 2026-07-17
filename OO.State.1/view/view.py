from tkinter import *
from tkinter import ttk, colorchooser


class View:
    def __init__(self):
        self.root = Tk()
        self.criar_interface()

    def executar(self):
        self.root.mainloop()


        # abre o seletor de cor e atualiza tanto a variável quanto a cor de fundo do botão, pra dar um feedback visual de qual cor tá selecionada
    def escolher_cor_borda(self):
        cor = colorchooser.askcolor(title="Escolha a cor da borda", initialcolor=self.cor_borda_atual.get())
        # cor é uma tupla tipo ((r,g,b), '#hexadecimal'), só interessa o hexadecimal
        if cor[1] is not None:  # se a pessoa clicar em cancelar, cor[1] vem None, então não faz nada
            self.cor_borda_atual.set(cor[1])
            self.botao_cor_borda.config(bg=cor[1])

    def escolher_cor_preenchimento(self):
        cor_inicial = "#8c8488"
        if self.cor_preenchimento_atual.get():
            cor_inicial = self.cor_preenchimento_atual.get()
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
        label = ttk.Label(self.frame, text='Peinte')
        label.grid(column=0, row=0, sticky=W, **paddings)

        # option menu
        self.tipo_figura_var = StringVar(self.root)  # Guarda o tipo de figura selecionado no option menu
        option_menu = ttk.OptionMenu(self.frame, self.tipo_figura_var,
                                     'Linha', 'Linha', 'Rabisco', 'Círculo', 'Oval', 'Retângulo', 'Polígono')
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

    def obter_tipo_figura(self):
        return self.tipo_figura_var.get()

    def obter_cor_preenchimento(self):
        return self.cor_preenchimento_atual.get()
    
    def obter_cor_borda(self):
        return self.cor_borda_atual.get()


