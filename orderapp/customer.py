from random import randint
from time import time
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
        self._orders_list = list()
        self._is_active = True
        self._status_date = time()
        return None

    def __str__(self):
        return f'{self.name} {self.surname} {self.age}'

    def update_customer(self, n_name='', n_surname='', age=0):
        if n_name:
            self.name = n_name
        if n_surname:
            self.surname = n_surname
        if age:
            self.age = age
        return {
            'name': self.name,
            'surname': self.surname,
            'age': self.age
            }

    @property
    def remove_customer(self):
        self._is_active = False
        self._status_date = time()
        return f'Пользователь {self._customer_id} удалён'

    def create_order(self):
        order_id = len(self._orders_list)
        new_order = Order(order_id)
        self._orders_list.append(new_order)
        return new_order

    def checkout_order(self, order_id):
        spam = self._orders_list[order_id]
        if spam.get_status == 'Forming':
            spam.set_status('Paid')
        return spam.get_status

    def remove_order(self, order_id):
        spam = self._orders_list[order_id]._remove_order
        return spam
