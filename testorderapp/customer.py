from random import randint
from time import time
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))
from .order import Order


class Customer:
    """ Customer class for ecommerce """

    def __init__(self, name, surname, age):
        self._customer_id = randint(1000, 100000)
        self.name = name
        self.surname = surname
        self.age = age
        self._orders = list()
        self._is_active = True
        self._status_date = time()
        return None

    def __str__(self):
        return f'{self.name} {self.surname} {self.age}'

    def create_order(self):
        order_id = len(self.o_ordersrders) + 1
        new_order = Order(order_id)
        self.o_ordersrders.append(new_order)

    def remove_customer(self):
        self._is_active = False
        self._status_date = time()
        return f'Пользователь удалён'


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.name = 'Ivan'
        self.surname = 'Ivanov'
        self.age = 23

    def test_customer(self):
        user = Customer(self.name, self.surname, self.age)
        self.assertEqual(user.__str__(), f'{self.name} {self.surname} {self.age}')


if __name__ == "__main__":
    unittest.main()
