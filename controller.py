


class controller  :
    def __init__(self,view , model):
        self.view = view
        self.model = model


class main (controller) :
    
    "this is an example code for extending idea "
    
    def start(self):
        
        try:
            self.model.start()
            self.view.show_text("started ")
            
        except Exception as error:
            self.view.show_text("an error occured while starting")
