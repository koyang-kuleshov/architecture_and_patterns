from time import time

from testmainapp.items import Item


class Order:
    """ Class customer order """
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
        return f'Создан заказ №{self.order_id}'

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
    item_quantity = 0

    def __init__(self, orderitem_id, item_id, quantity):
        self._orderitem_id = orderitem_id
        self.item_id = Item(item_id)
        self.item_quntity += quantity
        return (f'Добавле товар {self.order_id} в количестве '
                f'{self.item_quntity}')

    def change_quantity(self, new_quantity):
        if self.item_quntity - new_quantity < 0:
            return f'Неверно задано количество товаров'
        self.item_quntity = new_quantity

    @staticmethod
    def get_orderitem_sum(self):
        return self.item.get_price * self.item_quntity
