from controller import Controller
from view import View
from model import Model


def main():
    view = View()
    model = Model()
    controller = Controller(model, view)

    view.setar_controller(controller)
    view.executar()

if __name__ == "__main__":
    main()