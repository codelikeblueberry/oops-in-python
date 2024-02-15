total = 0
def infinte_sum(func):
    def modified_function(*args): 
        global total       
        for num in args:
            total = total+num
        return total
    return modified_function

def string_result(func):
    def modified_function(*args):
        return f"The sum of those three numbers is {func(*args)}"
    return modified_function

@string_result
@infinte_sum
def sum(a,b):
    return a+b

print(sum(2,3,4,4,5,6,6)) 