# default __repr__and __str__ are dunder methods(casue they have underscores inandout) who return
# <modulename.classname object at memory address> both string values
# repr method kar output repr() function se access karte hain aur str ka str() se.
# print(type(str(item1))) #<class 'str'>
# print(type(repr(item1))) #<class 'str'>

class Item:
    discount_rate=0.75
    instance = []
    def __init__(self,name:str,price:float,quantity=0):
        # Run validation to received arguments
        assert price>=0 , f"The price {price} should be greater than or equal to 0"
        assert quantity>0 , f"The quantity {quantity} must be greater than 0"

        # Assign to the self object
        self.name = name
        self.price  = price
        self.quantity = quantity

        Item.instance.append(self) # here the append happening whatever is defined in the default __repr__() method. i,e. return f" <__main__.Item object at 0x0000020125ED30A0> "
        
    def __str__(self):
        return f'Item("{self.name}",{self.price},{self.quantity})'

    def bill(self):
        return self.price*self.quantity
    def discount(self):
        self.price=self.price*self.discount_rate


item1 = Item("Tomato",200,5)
item2 = Item("Potato",300,2)
item3 = Item("Ginger",100,2)
item4 = Item("Radish",400,1)
item5 = Item("Garlic",50,6)

print(Item.instance) # guess output
print(item1) # guess output
