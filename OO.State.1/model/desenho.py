class Desenho:
    def __init__(self):
        self.figuras = []
        self.figura_nova = None

    def desenhar(self, canvas):
        canvas.delete('all')
        for item in self.figuras:
            item.desenhar(canvas)
    
    def adicionar_figura(self, figura):
        self.figuras.append(figura)

    def obter_figuras(self):
        return self.figuras

    def obter_figura_nova(self):
        return self.figura_nova
