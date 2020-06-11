import unittest
from orderapp.customer import Customer
from orderapp.order import Order


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.name = 'Ivan'
        self.surname = 'Ivanov'
        self.age = 23
        self.user = Customer(self.name, self.surname, self.age)

    def test_customer(self):
        self.assertIsInstance(self.user, Customer)
        self.assertEqual(str(self.user), (f'{self.name} {self.surname} '
                                          f'{self.age}'))

    def test_update_customer(self):
        spam = self.user.update_customer('Petr', 'Petrov', 34)
        self.assertEqual(spam, {
            'name': 'Petr',
            'surname': 'Petrov',
            'age': 34
            }
        )

    def test_create_order(self):
        self.assertIsInstance(self.user.create_order(), Order)

    def test_checkout_order(self):
        self.test_create_order()
        self.assertNotEqual(self.user.checkout_order(0), 'Paid')
        self.user._orders_list[0].set_status('Forming')
        self.assertEqual(self.user.checkout_order(0), 'Paid')

    def test_remove_order(self):
        spam = self.test_create_order()
        self.assertEqual(self.user.remove_order(0), 'Заказ 0 удалён')

    def test_remove_customer(self):
        customer_id = self.user._customer_id
        spam = self.user.remove_customer
        self.assertEqual(spam, f'Пользователь {customer_id} удалён')


if __name__ == "__main__":
    unittest.main()
