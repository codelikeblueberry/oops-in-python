lst = [1,2,3,4]

def sum(a,b,c,d):
    print(a+b+c+d)

sum(*lst)

one,two,three,four, = lst.copy() # unpacking list
