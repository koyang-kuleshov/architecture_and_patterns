from random import randint
from time import time

from order import Order


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
        return f'Создан пользователь {name} {surname}'

    def __str__(self):
        return f'{self.name} {self.surname}'

    def create_order(self):
        order_id = len(self.o_ordersrders) + 1
        new_order = Order(order_id)
        self.o_ordersrders.append(new_order)

    def remove_customer(self):
        self._is_active = False
        self._status_date = time()
        return f'Пользователь удалён'


if __name__ == '__main__':
    user = Customer('Ivan', 'Ivanov', 23)
    print(user)
