
class model:
    pass

class main (model):
    "this is an example code for extending idea "
    
    def save_to_file( self,text):
           file = open("helo.txt","w")
           file.write(text)
           file.close()
           

