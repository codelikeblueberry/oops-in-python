# Class variable and instance variable
# Change in class variable Reflects in all instances
# changing rate for this instance only reflects only in that instance
# Hence both instance and class variables can be overridden

class Item:
    discount_rate=0.75
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
    def discount(self):
        bill=self.bill()
        return bill*Item.discount_rate

item1 = Item("Frock",400,2)
item2 = Item('Saree',1000,7)
item3 = Item('Jeans',600,3)



Item.discount_rate = 0.76
print(Item.discount_rate) # 0.76
item1.discount_rate = 0.70  # changing rate for this instance only reflects only in that instance
print(item1.discount_rate) # 0.7
print(item2.discount_rate) # 0.76 #Change in class variable Reflects in all instances
