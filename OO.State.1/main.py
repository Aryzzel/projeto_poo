from controller.controller import Controller
from view.view import View
from model.desenho import Desenho


def main():
    view = View()
    desenho = Desenho()
    controller = Controller(desenho, view)
    view.executar()
    

if __name__ == "__main__":
    main()