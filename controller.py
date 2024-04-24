class controller  :
    def __init__(self,view , model):
        self.view = view
        self.model = model


class example (controller) :
    
    "this is an example code "
    
    def run(self):
        
        try:
            text = self.view.ask_question("enter some text it will be saved to file")
            self.model.save_to_file(text)
            self.view.show_text("successfully writen to file")
            
        except Exception as error:
            self.view.show_text("an error occuered while saving to file")
