import view
import model
import controller


class mvc:
    def __init__(self):
        self.view = view.example()
        self.model = model.example()
        self.controller = controller.example(self.view, self.model)
        self.view.set_controller(self.controller)

class main(mvc):

    "entrypoint of this software .it is written in mvc design pattern"
    "extend this class and create your own implementation "

    def run(self):
            self.controller.run()

        



if __name__ == "__main__":
    main().run()
