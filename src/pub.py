class Pub:
    def __init__(self,name,cash):
        self.name = name
        self.cash = cash
        self.stock = [
            {"Guiness":{"alcohol_level":5,"stock":15}},
            "IPA":{"alcohol_level":4,"stock":20},
            "Wine":{"alcohol_level":9,"stock":10}
        ]

    def increase_cash(self,amount):
        self.cash += amount

    def decrease_cash(self,amount):
        self.cash -= amount

    def check_age(self, customer):
        return customer.age >= 18

    def check_drukenness(self,customer):
        return customer.drunkenness <= 50

    def check_stock(self, pub):
        total_stock = 0

        for drink in pub.stock["stock"]:
            total_stock += drink
        return total_stock
