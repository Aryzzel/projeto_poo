from controller.controller import Controller
from view.view import View
from model.model import Model


def main():
    view = View()
    model = Model()
    controller = Controller(model, view)
    view.executar()
    

if __name__ == "__main__":
    main()