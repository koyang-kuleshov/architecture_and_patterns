from time import time
import unittest

from mainapp.catalog import Item


class Order:
    """ Class customer order """
    _order_status_dict = {
        'Created': 'Created',
        'Forming': 'Forming',
        'Paid': 'Paid',
        }

    def __init__(self, order_id):
        self._order_id = order_id
        self._item_list = list()
        self._order_date = time()
        Order._order_status = self._order_status_dict["Created"]
        return None

    def __str__(self):
        return f'Заказ №{self._order_id}'

    def add_item(self, item_id=None, size='M', quantity=1):
        orderitem_id = len(self._item_list)
        new_item = OrderItem(orderitem_id, item_id, size, quantity)
        self._item_list.append(new_item)
        return {
                'item_id': orderitem_id,
                'orderitem_name': new_item.orderitem.item_name,
                'orderitem_price': new_item.orderitem.get_price,
                'orderitem_size': new_item.orderitem_size,
                'orderitem_quantity': new_item.orderitem_quantity
        }

    def update_orderitem(self, orderitem_id, size='', quantity=0):
        return self._item_list[orderitem_id].update_orderitem(size, quantity)

    def remove_item(self, orderitem_id):
        spam = self._item_list[orderitem_id]
        del self._item_list[orderitem_id]
        return spam

    @property
    def get_summary(self):
        sum_quantity = sum(map(lambda q: q.orderitem_quantity,
                               self._item_list))
        summary = sum(map(lambda x: x.get_orderitem_sum['orderitem_summary'],
                          self._item_list))
        return f'Всего товаров {sum_quantity}, на сумму {summary} руб.'

    @property
    def get_status(self):
        return self._order_status

    def set_status(self, new_status):
        try:
            spam = self._order_status_dict.get(new_status)
        except KeyError:
            return spam
        else:
            self._order_status = spam
        return self._order_status

    @property
    def _remove_order(self):
        self._order_status = 'Canceled'
        return f'Заказ {self._order_id} удалён'


class OrderItem:
    """ Item of order. Contains good and quantity """

    def __init__(self, orderitem_id, item_id, size, quantity=1):
        self._orderitem_id = orderitem_id
        self.orderitem = Item.item_list[item_id]
        self.orderitem_size = size
        self.orderitem_quantity = quantity
        return None

    def update_orderitem(self, new_size, new_quantity):
        if new_size:
            self.orderitem_size = new_size
        if self.orderitem_quantity - new_quantity > 0:
            self.orderitem_quantity = new_quantity
        return {
                'orderitem_size': self.orderitem_size,
                'orderitem_quantity': self.orderitem_quantity
        }

    @property
    def get_orderitem_sum(self):
        return {
            'orderitem': self.orderitem,
            'orderitem_quantity': self.orderitem_quantity,
            'orderitem_summary': self.orderitem.get_price *
            self.orderitem_quantity
        }


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
        self.assertEqual(self.order.get_summary,
                         f'Всего товаров 7, на сумму 0 руб.'
                         )

    def test_get_status(self):
        self.assertEqual(self.order.get_status, (f'Статус заказа '
                         f'{self.order._order_status}')
                         )

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
