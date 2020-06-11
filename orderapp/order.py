from time import time

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
        self._order_status = Order._order_status_dict["Created"]

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

