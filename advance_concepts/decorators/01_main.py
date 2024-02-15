def other_function(func): # decorator
    def modified_func(a,b,c):
        funct = func(a,b) + c # here the new parameter is introduced and modified the result
        return f"The sum of two numbers is {funct}" # result 2
    return modified_func
@other_function
def function(a,b):
    return a+b # result 1

print(function(100,100,100)) #jab tumne isko decorate kar diya tha ye 3 arguments lene laga

