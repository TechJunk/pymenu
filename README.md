# pymenu
Make simple CLI menus in python  
  
Paste the function into your code and call it like this  

> menu("What is your name",[["John",johncallback],["Not John",notjohncallback]])
  
Where you have the following defined:  

> def johncallback(): print("Hello John")  
> def notjohncallback(): print("You are not john")

Output in this example:  

> What is your name  
> \=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=  
> 1\) John  
> 2\) Not John  
> >**1**  
>   
> Hello John  

Or

> What is your name  
> \=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=\=  
> 1\) John  
> 2\) Not John  
> > **2**  
>   
> You are not john  
