import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Codeclan Pub",1000)
        self.customer = Customer("Karl",50,49)
        self.drink = Drink("Guiness", 10, 5)
    
    def test_increase_cash(self):
        self.pub.increase_cash(5)
        self.assertEqual(1005,self.pub.cash)

    def test_decrease_cash(self):
        self.pub.decrease_cash(5)
        self.assertEqual(995,self.pub.cash)

    def test_check_age(self):
        self.assertEqual(True, self.pub.check_age(self.customer))

    def test_check_drunkenness(self):
        self.assertEqual(True,self.pub.check_drukenness(self.customer))

    def test_check_stock(self):
        stock = self.pub.check_stock(self.pub)
        self.assertEqual(45, stock)