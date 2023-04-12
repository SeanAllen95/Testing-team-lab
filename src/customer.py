class Customer:
    def __init__(self, name, wallet,age):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def buy_a_drink(self, drink, pub):
        self.reduce_wallet(drink.price)
        pub.cash += drink.price
        self.drunkenness += drink.alcohol_level

    def buy_food(self, food, pub):
        self.reduce_wallet(food.price)
        self.drunkenness -= food.rejuvenation
        pub.cash += food.price
    
    

