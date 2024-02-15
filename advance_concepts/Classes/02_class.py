# Validation of arguments in the instance of class.


class Item:
    def __init__(self,name:str,price:float,quantity=0):
        # Run validation to received arguments
        assert price>=0 , f"The price {price} should be greater than or equal to 0"
        assert quantity>0 , f"The quantity {quantity} must be greater than 0"

        # Assign to the self object
        self.name = name
        self.price  = price
        self.quantity = quantity

    def bill(self):
        return self.price*self.quantity

item1 = Item("Frock",400,2)
item2 = Item('Saree',1000,7)
item3 = Item('Jeans',600,3)

print(item1.bill())
