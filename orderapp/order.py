from time import time
import unittest

from mainapp.catalog import Item


class Order:
    """ Class customer order """
    orderitem_list = []
    _order_status_dict = {
        'Created': 'Created',
        'Forming': 'Forming',
        'Paid': 'Paid',
        }

    def __init__(self, order_id):
        self._order_id = order_id
        self._items = list()
        self._order_date = time()
        self._order_status = self.order_status_dict["Created"]
        return None

    def __str__(self):
        return f'Заказ №{self.order_id}'

    def add_item(self, item_id=None, quantity=1):
        orderitem_id = len(self.items) + 1
        new_item = OrderItem(orderitem_id, item_id, quantity)
        self._items.append(new_item)
        return f'Добавлен товар №{self.orderitem_id}'

    def remove_item(self, orderitem_id):
        del self._items[orderitem_id]
        return f'Удалён товар №{self.orderitem_id}'

    @staticmethod
    def get_summary(self):
        sum_quantity = sum(map(lambda q: q.item_quantity, self._items))
        summary = sum(map(lambda x: x.get_orderitem_sum, self._items))
        return f'Всего товаров {sum_quantity}, на сумму {summary} руб.'

    @staticmethod
    def get_status(self):
        return f'Статус заказа {self._order_status}'

    def set_status(self, new_status):
        try:
            self._order_status = self._order_status_dict.get(new_status)
        except KeyError:
            print('Неверный статус')

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
