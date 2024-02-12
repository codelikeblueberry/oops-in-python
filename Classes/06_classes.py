# after defined 0 for a instance , the discount method was taking class variable
# so we need to chane it to self.dicount_rate to take instrance variable first to then go for class var
# now observe changes in the price
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
        self.price=self.price*self.discount_rate


item1 = Item("Frock",400,2)
item2 = Item('Saree',1000,7)
item3 = Item('Jeans',600,3)

item1.discount() # After applying discount (0.75)
print(item1.price)
print("----------")


item3.discount()
print(item3.price)
print(item3.discount_rate)
print("----------")
item2.discount_rate = 0
item2.discount()
print(item2.price)
print(item2.discount_rate)
