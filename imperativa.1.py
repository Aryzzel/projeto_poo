from tkinter import *
from tkinter import ttk
from tkinter import colorchooser  # pra abrir aquela paleta de cores nativa do tkinter

# Quando mouse é pressionado
def iniciar_figura_nova(event):
    global figura_nova
    cor = cor_borda_atual.get()  # pega a cor que tá selecionada no momento do clique
    if tipo_figura_var.get() == 'Linha':
        figura_nova = ("linha", (event.x, event.y, event.x, event.y), cor)
    elif tipo_figura_var.get() == 'Rabisco':
        figura_nova = ("rabisco", [(event.x, event.y)], cor)
    elif tipo_figura_var.get() == 'Círculo':
        figura_nova = ("circulo", (event.x, event.y, event.x), cor)
    elif tipo_figura_var.get() == 'Oval':
        figura_nova = ("oval", (event.x, event.y, event.x, event.y), cor)
    elif tipo_figura_var.get() == 'Retângulo':
        figura_nova = ("retangulo", (event.x, event.y, event.x, event.y), cor)


# Quando mouse é movido com o botão pressionado
def atualizar_figura_nova(event):
    global figura_nova
    cor = figura_nova[2]  # mantém a cor que já foi escolhida lá no início, não deixa mudar no meio do desenho
    if figura_nova[0] == "rabisco":
        figura_nova[1].append((event.x, event.y))
    elif figura_nova[0] == "linha":
        figura_nova = ("linha", (figura_nova[1][0], figura_nova[1][1], event.x, event.y), cor)
    elif figura_nova[0] == "circulo":
        figura_nova = ("circulo", (figura_nova[1][0], figura_nova[1][1], abs(figura_nova[1][0]+figura_nova[1][1] - (event.x+event.y))), cor)
    elif figura_nova[0] == "oval":
        figura_nova = ("oval", (figura_nova[1][0], figura_nova[1][1], abs(figura_nova[1][0] - event.x), abs(figura_nova[1][1]- event.y)), cor)
    elif figura_nova[0] == "retangulo":
        figura_nova = ("retangulo", (figura_nova[1][0], figura_nova[1][1], event.x, event.y), cor)
    desenhar_figuras()
    desenhar_figura_nova()

# Quando mouse é solto
def incluir_figura_nova(event): 
    if not incompleta(figura_nova): # para evitar incluir figuras incompletas, como uma linha sem comprimento ou um rabisco com um único ponto
        figuras.append(figura_nova) 
    desenhar_figuras()

def desenhar_figuras():
    canvas.delete("all")
    # cada figura agora vem com uma cor junto, por isso o for desempacota 3 valores e não mais 2
    for fig, values, cor in figuras:
        if fig == "linha":
            canvas.create_line(values[0], values[1], values[2], values[3], fill=cor)  # em linha, fill é a cor do traço mesmo (não tem outline)
        elif fig == "rabisco":
            canvas.create_line(values, fill=cor)
        elif fig == "circulo":
            canvas.create_oval(values[0]-values[2], values[1]-values[2], values[0]+values[2], values[1]+values[2], outline=cor)  # outline = cor da borda
        elif fig == "oval":
            canvas.create_oval(values[0]-values[2], values[1]-values[3], values[0]+values[2], values[1]+values[3], outline=cor)
        elif fig == "retangulo":
            canvas.create_rectangle(values[0], values[1], values[2], values[3], outline=cor)

def desenhar_figura_nova():
    fig, values, cor = figura_nova
    if fig == "linha":
        canvas.create_line(values[0], values[1], values[2], values[3], fill=cor, dash=(4, 2))
    elif fig == "rabisco":
        canvas.create_line(values, fill=cor, dash=(4, 2))
    elif fig == "circulo":
        canvas.create_oval(values[0]-values[2], values[1]-values[2], values[0]+values[2], values[1]+values[2], outline=cor, dash=(4,2))
    elif fig == "oval":
        canvas.create_oval(values[0]-values[2], values[1]-values[3], values[0]+values[2], values[1]+values[3], outline=cor, dash=(4,2))
    elif fig == "retangulo":
        canvas.create_rectangle(values[0], values[1], values[2], values[3], outline=cor, dash=(4,2))

def incompleta(figura):
    fig, values, cor = figura  # cor não é usada aqui, só serve pra desempacotar certo
    if fig == "linha":
        return (values[0], values[1]) == (values[2], values[3])
    elif fig == "rabisco":
        return len(values) <= 1
    elif fig == "circulo" or fig == "oval":
        return (values[0] == values[2])
    elif fig == "retangulo":
        return (values[0], values[1]) == (values[2], values[3])

# abre o seletor de cor e atualiza tanto a variável quanto a cor de fundo do botão, pra dar um feedback visual de qual cor tá selecionada
def escolher_cor_borda():
    cor = colorchooser.askcolor(title="Escolha a cor da borda", initialcolor=cor_borda_atual.get())
    # cor é uma tupla tipo ((r,g,b), '#hexadecimal'), só interessa o hexadecimal
    if cor[1] is not None:  # se a pessoa clicar em cancelar, cor[1] vem None, então não faz nada
        cor_borda_atual.set(cor[1])
        botao_cor_borda.config(bg=cor[1])


#******* MAIN *******#

figuras = []       # Todas as figuras desenhadas
figura_nova = None # Figura que está sendo desenhada, mas ainda não foi incluída em figuras

root = Tk()
frame = Frame(root)

# Widgets arranjados com Layout grid dentro de frame
paddings = {'padx': 5, 'pady': 5} 

# label
label = ttk.Label(frame,  text='Linha ou Rabisco:')
label.grid(column=0, row=0, sticky=W, **paddings)

# option menu
tipo_figura_var = StringVar(root) # Guarda o tipo de figura selecionado no option menu (linha ou rabisco)
option_menu = ttk.OptionMenu(frame, tipo_figura_var,
                             'Linha', 'Linha', 'Rabisco', 'Círculo', 'Oval', 'Retângulo')
option_menu.grid(column=1, row=0, sticky=W, **paddings)

# bordas com cor
cor_borda_atual = StringVar(root, value='#000000')  # guarda a cor escolhida em hexadecimal ('#ff0000'), começa preto igual o padrão do tkinter
botao_cor_borda = Button(frame, text='Cor da Borda', command=escolher_cor_borda, # botao que abre a paleta de cores; o bg dele serve de "preview" mostrando a cor atual
                          bg=cor_borda_atual.get())
botao_cor_borda.grid(column=2, row=0, sticky=W, **paddings)

# Área de desenho
canvas = Canvas(frame, bg='white', width=600, height=600)
canvas.grid(column=0, row=1, columnspan=3, sticky=W, **paddings)

frame.pack()

# Eventos de mouse associados ao canvas - com seus callbacks
canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)

root.mainloop()