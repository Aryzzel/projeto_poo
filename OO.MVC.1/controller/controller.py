from model.figuras import Linha, Rabisco, Circulo, Oval, Retangulo, Poligono


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Eventos de mouse associados ao canvas - com seus callbacks
        self.view.canvas.bind('<ButtonPress-1>', self.iniciar_figura)
        self.view.canvas.bind('<Motion>', self.atualizar_poligono)
        self.view.canvas.bind('<B1-Motion>', self.atualizar_figura)
        self.view.canvas.bind('<ButtonRelease-1>', self.incluir_figura)
        self.view.canvas.bind('<Double-Button-1>', self.finalizar_poligono)  # duplo-clique fecha o polígono
        self.view.root.mainloop()

    def iniciar_figura(self, event):
        tipo = self.view.obter_tipo_figura()
        x = event.x
        y = event.y
        cor_borda = self.view.obter_cor_borda()
        cor_preenchimento = self.view.obter_cor_preenchimento()

        if tipo == "Polígono":
            if isinstance(self.model.figura_nova, Poligono):
                self.model.figura_nova.adicionarPonto((x, y))
                self.model.figura_nova.coordenadas[0] = (x, y)
                self.model.figura_nova.coordenadas[1] = (x, y)
                self.model.desenhar(self.view.canvas)
                self.model.figura_nova.desenhar(self.view.canvas,tracejado=(4,2))

            else:
                self.model.figura_nova = Poligono(
                    [(x, y), (x, y)],
                    [(x, y)],
                    cor_borda,
                    corFill=cor_preenchimento
                )
            return

        if tipo == "Linha":
            self.model.figura_nova = Linha([x, y, x, y], cor_borda, cor_preenchimento)
        elif tipo == "Rabisco":
            self.model.figura_nova = Rabisco([(x, y)], cor_borda, cor_preenchimento)
        elif tipo == "Círculo":
            self.model.figura_nova = Circulo([x, y, x, y], cor_borda, cor_preenchimento)
        elif tipo == "Oval":
            self.model.figura_nova = Oval([x, y, x, y], cor_borda, cor_preenchimento)
        elif tipo == "Retângulo":
            self.model.figura_nova = Retangulo([x, y, x, y], cor_borda, cor_preenchimento)


    def atualizar_figura(self, event):
        if self.model.figura_nova is None:
            return

        if isinstance(self.model.figura_nova, Rabisco):
            self.model.figura_nova.adicionarPonto((event.x, event.y))
        else:
            self.model.figura_nova.alterarPontosFinais(event.x, event.y)

        
        self.model.desenhar(self.view.canvas)
        self.model.figura_nova.desenhar(self.view.canvas,tracejado=(4,2))


    def atualizar_poligono(self, event):
        if isinstance(self.model.figura_nova, Poligono):
            self.atualizar_figura(event)

    def incluir_figura(self, event):
        if self.model.figura_nova is None or isinstance(self.model.figura_nova, Poligono):
            return

        if not self.model.figura_nova.incompleta():
            self.model.adicionar_figura(self.model.figura_nova)

        self.model.figura_nova = None
        self.model.desenhar(self.view.canvas)

    def finalizar_poligono(self, event):
        if not isinstance(self.model.figura_nova, Poligono):
            return

        if not self.model.figura_nova.incompleta():
            self.model.figura_nova.completo = True
            self.model.adicionar_figura(self.model.figura_nova)

        self.model.figura_nova = None
        self.model.desenhar(self.view.canvas)



