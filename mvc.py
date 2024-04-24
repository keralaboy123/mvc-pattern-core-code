import view
import model
import controller


class mvc:
    
    "entrypoint of this software .it is written in mvc design pattern"
    "extend this class and create your own implementation "
    
    def __init__(self):
        self.view = view.view()
        self.model = model.model()
        self.controller = controller.controller(self.view, self.model)
        self.view.set_controller(self.controller)


class example(mvc):
    
    "this is an example code"
    
    def __init__():
        self.view = view.example()
        self.model = model.example()
        self.controller = controller.example(self.view, self.model)
        self.view.set_controller(self.controller)

    def run(self):
        self.controller.run()

        



if __name__ == "__main__":
    example().run()
