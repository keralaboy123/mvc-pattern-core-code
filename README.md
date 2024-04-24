# mvc-pattern-core-code
these files are used for creating mvc style professional code from simple class in python language.

written in easy to understand way. just save these files into your project folder ,import classes and  use inheritance to extend its functions.



### what is mvc design pattern
<pre>
   it a way of writing code .it is a way  to create a professional or 
   easly maintainable and easy to understand code 
   to do it we should seperate code into 3 things.called model view and controller.
   
   it means
      * we must start execution from controller. 
      * controller will start graphical user interface (view functions)
      * it will also start core backend code ( model functions).
      * we should not call model functions from view and we should not call view functions from model. 
      * controller can call view and model functions. so they can communicate
   if you implemented this basic code then it automaticaly becomes a professional code
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

