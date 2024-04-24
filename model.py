
class model:
    pass

class example (model):
    "this is an example code "
    
    def save_to_file( self,text):
           file = open("helo.txt","w")
           file.write(text)
           file.close()
           

