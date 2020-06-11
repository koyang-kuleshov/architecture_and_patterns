import unittest

from orderapp.order import Order, OrderItem
from mainapp.catalog import Item


class TestOrder(unittest.TestCase):

    def setUp(self):
        self.order_id = 0
        Item(0, 0, '1BLCXL', 'Куртка', 'XL')
        self.order = Order(self.order_id)
        self.orderitem = OrderItem(0, 0, 'S', 3)

    def test_order(self):
        self.assertIsInstance(self.order, Order)
        self.assertEqual(str(self.order),
                         f'Заказ №{self.order._order_id}'
                         )

    def test_add_item(self):
        self.test_order()
        self.assertIsInstance(self.order.add_item(0, 'M', 7), dict)

    def test_get_summary(self):
        self.test_add_item()
        self.assertIsInstance(self.order.get_summary, str)

    def test_get_status(self):
        self.assertEqual(self.order.get_status, self.order._order_status)

    def test_set_status(self):
        self.assertEqual(self.order.set_status('Forming'), 'Forming')
        self.assertIsNone(self.order.set_status('Deliver'), 'Created')

    def test_remove_order(self):
        self.assertEqual(self.order._remove_order,
                         f'Заказ {self.order._order_id} удалён')


class TestOrderItem(unittest.TestCase):

    def setUp(self):
        Item(0, 0, '1BLCXL', 'Куртка', 'XL')
        self.orderitem = OrderItem(0, 0, 'S', 4)

    def test_orderitem(self):
        self.assertIsInstance(self.orderitem.orderitem, Item)

    def test_update_orderitem(self):
        self.assertIsInstance(self.orderitem.update_orderitem('M', 1), dict)

    def test_orderitem_sum(self):
        self.assertEqual(self.orderitem.get_orderitem_sum,
                         {
                          'orderitem': self.orderitem.orderitem,
                          'orderitem_quantity': 4,
                          'orderitem_summary': self.orderitem.orderitem.
                          get_price * 4
                         })


if __name__ == "__main__":
    unittest.main()
