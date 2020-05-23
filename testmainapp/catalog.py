from abc import ABC, abstractmethod
from random import randrange


class Catalog:
    category_list = list()

    def __init__(self):
        self.currency_rate = randrange(65, 80)

    def create_category(cls, name):
        category_id = len(cls.category_list)
        new_category = Category(category_id, name)
        cls.category_list.append(new_category)
        return f'Создана категория {category_id} {name}'

    def show_category(self, category_id):
        return self.category_list[category_id]

    def update_category(self, cls, category_id, name='', price_modifier=0,
                        remove=False):
        cat = cls.category_list[category_id]
        if remove:
            cat._is_active = False
            return (f'Категория {cat} {cat.name} удалена')
        if not name:
            cat.name = name
        if price_modifier != 0:
            cat._price_modifier = price_modifier
        return f'Категория изменена: {cat} {cat.name} {cat._price_modifier}'

    def _remove_category(cls, category_id):
        cls.category_list[category_id].is_active = False
        del cls.category_list[category_id]

    @property
    def fetch_currency_rate(self):
        self.currency_rate = randrange(65, 80)
        return self.currency_rate

    def search(self):
        pass


class Category:
    def __init__(self, category_id, name, price_modifier=1.0):
        self.cagetory_id = category_id
        self.name = name
        self._price_modifier = price_modifier
        self.category_items = list()
        self._is_active = True

    def add_category_item(self, item_style, item_name):
        new_item = Item(self.category_id, item_style, item_name)
        self.category_items.append(new_item)

    def show_items(self):
        return self.category_items

    def remove_category_item(self, item_id):
        del self.category_items[item_id]

    def _set_price_modifier(self, price_modifier):
        self._price_modifier = price_modifier


class GoodItem(ABC):

    @abstractmethod
    def _get_fabric_price(self):
        pass

    @abstractmethod
    def _set_fabric_price(self):
        pass

    @abstractmethod
    def _get_currency_rate(self):
        pass

    @abstractmethod
    def _set_price(self):
        pass

    @abstractmethod
    def get_price(self):
        pass


class Item(GoodItem):
    item_list = list()
    item_id = 0

    def __init__(self, category_id, item_style, item_name):
        self.category_id = category_id
        self.item_id += 1
        self.item_style = item_style
        self.item_name = item_name
        self._fabric_price = 1
        self.item_list.append(self)
        return None

    def __str__(self):
        return (f'{self.category_id}: {self.item_id} {self.item_style} '
                f'{self.item_name} {self.get_price} руб.')

    def update_category_item(cls, item_id, item_style='', item_name=''):
        if item_style != '':
            cls.item_list[item_id] = item_style
        elif item_name != '':
            cls.item_list[item_id] = item_name

    @property
    def _get_fabric_price(self):
        self._fabric_price = randrange(2, 300)
        return self._fabric_price

    def _set_fabric_price(self):
        self._fabric_price = float(input('Введите закупочную стоимость: '))

    def get_price(self):
        self.price = Catalog.currency_rate * self._fabric_price
