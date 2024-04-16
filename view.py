
class view:
    "extend this code "
    
    def set_controller(self, controller):
        self.controller = controller

    def __init__(self):
        self.controller = None

class main (view):
    "this is example usage of view "
    
    def ask_question(self,text):
        return input(text)
    
    def show_text(self,text):
        print (text)

