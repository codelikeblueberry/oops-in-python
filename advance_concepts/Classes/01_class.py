# Here we are showing the shop in which you provide the item and it
# gives the bill when you provide the price and quantity


class Item:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price  = price
        self.quantity = quantity

    def bill(self):
        return self.price*self.quantity

item1 = Item("Frock",400,2)
item2 = Item('Saree',1000,7)
item3 = Item('Jeans',600,3)

print(item1.bill())
