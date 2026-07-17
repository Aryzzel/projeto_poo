class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def iniciar_figura(self, event):
        self.model.iniciar_figura(
            self.view.obter_tipo_figura(),
            event.x,
            event.y,
            self.view.obter_cor_borda(),
            self.view.obter_cor_preenchimento()
        )
        self.atualizar_tela()

    def atualizar_figura(self, event):
        self.model.atualizar_figura(event.x, event.y)
        self.atualizar_tela()

    def atualizar_poligono(self, event):
        if self.model.poligono_em_construcao():
            self.model.atualizar_figura(event.x, event.y)
            self.atualizar_tela()

    def incluir_figura(self, event):
        self.model.finalizar_figura()
        self.atualizar_tela()

    def finalizar_poligono(self, event):
        self.model.finalizar_poligono()
        self.atualizar_tela()

    def atualizar_tela(self):
        self.view.desenhar_figuras(
            self.model.obter_figuras(),
            self.model.obter_figura_nova()
        )