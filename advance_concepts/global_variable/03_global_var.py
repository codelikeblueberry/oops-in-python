def Nemo():
    def Temo():
        a=8
        return a+var2   
    print(Temo())

#Nemo() # GIVING ERROR BECAUSE THE var2 IS NOT DECLARED GLOABALLY BEFORE THE FUNCITON IS CALLED!

var2 = 100
def Demo():
    a=8+var2
    print(a)


Nemo() # NOT GIVING ERROR BECAUSE THE var2 IS DECLARED GLOBALLY BEFORE THE FUNCTION IS CALLED!
Demo()

# IT DOESNT MATTER WHERE YOU ARE DECALARING THE GLOBAL VARIBALE DECLARE IT BEFORE CALLING THE FUNCITON

i=0
def function():   
    def sum_func():
        global i
        for j in range(10):
            i = i+j
        return i
    return function

func = function() # returns a sum_function which is assigned to func
func() # calling func variable
        
# work of global keyword 
# 1. Resist to make the global assigned varibale in the scope instead it tells that please global
# globally and take that variable
