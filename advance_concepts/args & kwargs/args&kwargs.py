lst = [1,2,3,4]

def sum(a,b,c,d):
    print(a+b+c+d)

sum(*lst)

one,two,three,four, = lst.copy() # unpacking list

# Q. 1 in asterick_operations.txt

lst2 = [1,2,3,4,5,6,7,8,9]
a,*c,b=lst2
print(a)
print(b)
print(c)

# Q. 1 in dictonaries.txt calculate sum of all fruits. using ** operator

fruits = {'apple':1,'banana':2,'pear':3}

def sumof(**para):
    new = [item for item in para]
    return new,para
print(sumof(apple=1,banana=2,pear=3,jamun=10))

# OUTPUT : (['apple', 'banana', 'pear', 'jamun'], {'apple': 1, 'banana': 2, 'pear': 3, 'jamun': 10})

# Query is it packing the keyword arguments here? Yes it is packing it into dictionary.
# But to pack them into a container like list tuple or set you have to use a function or their syntax
