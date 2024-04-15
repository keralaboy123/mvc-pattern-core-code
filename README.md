# mvc-pattern-core-code
it is for creating mvc style professional code from simple class in python language.
easy to understand


### what is mvc design pattern
<pre>
   it a way of writing code .it is a way  to create a professional or easly maintainable and easy to understand code 
   to do it we should seperate code into 3 things.called model view and controller.
   it means
      we must start execution from controller. controller will start graphical user interface (view functions)
      and it will start core backend code ( model functions).
      we should not call model functions from view and we should not call view functions from model. 
      controller is responsible for managing thse seperated codes communicatin
</pre>

### what are these files
<pre>
   mvc.py  
      it contain starting point .the main code
   
   model.py
    contain backend code or code which uses lowlevel api .
   
   view.py
      contains graphical user interface
   
   controller.py
      it contain business logic
      code responsible for managing model and view.
      means graphical inputs will trigger function inside controller and 
      controller will call functions inside model then responce willbe sended to view functions
      
</pre>

