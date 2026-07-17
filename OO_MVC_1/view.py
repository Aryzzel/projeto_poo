from tkinter import *
from tkinter import ttk


class View:
    def __init__(self):
        self.root = Tk()

    def setar_controller(self, controller):
        self.Controller = controller

    def executar(self):
        self.criar_interface()
        self.root.mainloop()

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
        self.botao_cor_borda = Button(self.frame, text='Cor da Borda', command=self.Controller.escolher_cor_borda,
                                      # botao que abre a paleta de cores; o bg dele serve de "preview" mostrando a cor atual
                                      bg=self.cor_borda_atual.get())
        self.botao_cor_borda.grid(column=2, row=0, sticky=W, **paddings)

        self.cor_preenchimento_atual = StringVar(self.root, value="")
        self.botao_cor_preenchimento = Button(self.frame, text='Preenchimento', command=self.Controller.escolher_cor_preenchimento)
        self.botao_cor_preenchimento.grid(column=3, row=0, sticky=W, **paddings)

        self.botao_sem_preenchimento = Button(self.frame, text='Transparente', command=self.Controller.remover_preenchimento)
        self.botao_sem_preenchimento.grid(column=3, row=1, sticky=W, **paddings)

        # Área de desenho
        self.canvas = Canvas(self.frame, bg='white', width=600, height=600)
        self.canvas.grid(column=0, row=2, columnspan=5, sticky=W, **paddings)

        self.frame.pack()

        # Eventos de mouse associados ao canvas - com seus callbacks
        self.canvas.bind('<ButtonPress-1>', self.Controller.iniciar_figura_nova)
        self.canvas.bind('<Motion>', self.Controller.atualizar_poligono)
        self.canvas.bind('<B1-Motion>', self.Controller.atualizar_figura_nova)
        self.canvas.bind('<ButtonRelease-1>', self.Controller.incluir_figura_nova)
        self.canvas.bind('<Double-Button-1>', self.Controller.finalizar_poligono)  # duplo-clique fecha o polígono
