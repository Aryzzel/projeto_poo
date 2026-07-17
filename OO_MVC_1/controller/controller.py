from OO_MVC_1.model.figuras import Linha, Rabisco, Circulo, Oval, Retangulo, Poligono


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

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
            else:
                self.model.figura_nova = Poligono(
                    [(x, y), (x, y)],
                    [(x, y)],
                    cor_borda,
                    corFill=cor_preenchimento
                )
            self.atualizar_tela()
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

        self.atualizar_tela()

    def atualizar_figura(self, event):
        if self.model.figura_nova is None:
            return

        if isinstance(self.model.figura_nova, Rabisco):
            self.model.figura_nova.adicionarPonto((event.x, event.y))
        else:
            self.model.figura_nova.alterarPontosFinais(event.x, event.y)

        self.atualizar_tela()

    def atualizar_poligono(self, event):
        if self.model.poligono_em_construcao():
            self.model.figura_nova.alterarPontosFinais(event.x, event.y)
            self.atualizar_tela()

    def incluir_figura(self, event):
        if self.model.figura_nova is None or isinstance(self.model.figura_nova, Poligono):
            return

        if not self.model.figura_nova.incompleta():
            self.model.figuras.append(self.model.figura_nova)

        self.model.figura_nova = None
        self.atualizar_tela()

    def finalizar_poligono(self, event):
        if not isinstance(self.model.figura_nova, Poligono):
            return

        if not self.model.figura_nova.incompleta():
            self.model.figura_nova.completo = True
            self.model.figuras.append(self.model.figura_nova)

        self.model.figura_nova = None
        self.atualizar_tela()

    def atualizar_tela(self):
        self.view.desenhar_figuras(
            self.model.obter_figuras(),
            self.model.obter_figura_nova()
        )