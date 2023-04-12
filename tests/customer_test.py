import unittest
from src.customer import Customer
from src.pub import Pub
from src.drink import Drink
from src.food import Food

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Karl",50,49)
        self.pub = Pub("Codeclan pub",1000)
        self.drink = Drink("Guinness", 10, 5)
        self.food = Food("Chips",2,3)

    def test_reduce_wallet(self):
        self.customer.reduce_wallet(5)
        self.assertEqual(45, self.customer.wallet)

    def test_buy_a_drink(self):
        self.customer.buy_a_drink(self.drink,self.pub)
        self.assertEqual(40, self.customer.wallet)
        self.assertEqual(1010,self.pub.cash)
        self.assertEqual(5, self.customer.drunkenness)
        
    def test_buy_food(self):
        self.customer.buy_a_drink(self.drink,self.pub)
        self.customer.buy_food(self.food,self.pub)
        self.assertEqual(38,self.customer.wallet)
        self.assertEqual(2 ,self.customer.drunkenness)
        self.assertEqual(1012 ,self.pub.cash)

    