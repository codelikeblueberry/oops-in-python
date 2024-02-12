item1_name = "car"
price1 = 1000
quantity1 = 2

item2_name = "bike"
price2 = 3000
quantity2 = 3

item3_name = "plane"
price3 = 2000
quantity3 = 8

item4_name = "laptop"
price4 = 100
quantity4 = 2

item5_name = "drier"
price5 = 300
quantity5 = 9

def budget(price, quantity):
    return price * quantity


# budget3 = budget(price3, quantity3)
# print(budget3)

# instead we use classes to make these same kind of items like-books,laptops,vehicles
# shoes,clothes, outdoor_games, indoor_games, restaurent_menu, web_browsers, playstore_apps(installed/uninstalld, average_screentime)
# tourist_sites, countries, IDEs, programming_languages, etc.
# calculation, shopping, gaming, online_payment,etc
# calculation = mathemtical solution laane ko fast karti h
# shopping = varietry_choices, less_human_effort, track_sales
# gaming = fun, socialize, concentraion buuilding.
# payment = fast, global, immediate, secure, record, etc.

# Okay to make you understand this concept more let me give you the scenario.
# there are is a dhaba where limited amount of thaali are there and the menu is given
# paneer-butter-masala-daal-4roti-chawal = 120
# jeera-aloo-daal-4roti= 100
# roti,paani = 10,20
# output total bill calcuate.

#  IF THE DHABA HAS THE SAME MENU
class Dhaba:
    def __init__(self):
        self.menu ={'thali1':100,'thali2':150,'roti':5,'pani':20}

    def bill(self,order:dict):
        total =0
        for item,qty in order.items():
            price = self.menu.get(item)
            total = total+price*qty
        return total
cls1 = Dhaba()
bill = cls1.bill({'thali1':2,'pani':2,'roti':3})
print(bill)
# IF THE DHABA HAS THE DIFFERENT MENU
class Dhaba:
    def __init__(self,menu):
        self.menu =menu
    def bill(self,order:dict):
        total =0
        for item,qty in order.items():
            price = self.menu.get(item)
            total = total+price*qty
        return total
cls1 = Dhaba({'thali1':101,'thali2':151,'roti':8,'pani':22})
bill = cls1.bill({'thali1':2,'pani':2,'roti':3})
print(bill)
# Here you can see that only the input is coming different when we change the menu but the structure of
# calulation of the bill of any dhaba is remaining the same

