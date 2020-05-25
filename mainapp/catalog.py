from abc import ABC, abstractmethod
from random import randrange
import unittest


class Catalog:
    currency_rate = 0
    category_list = list()

    def __init__(self):
        Catalog.currency_rate = self.fetch_currency_rate
        return None

    def __str__(self):
        return str({'currency_rate': self.currency_rate,
                    'category_list': Catalog.category_list})

    def show_category(cls, category_id):
        return cls.category_list[category_id]

    @property
    def fetch_currency_rate(self):
        self.currency_rate = randrange(65, 80) * 0.99
        return self.currency_rate

    def show_all_categories(cls):
        return {'categories': cls.category_list}

    def search(self):
        pass


class Category:
    def __init__(self, category_id, name, price_modifier=1.0):
        self.category_id = category_id
        self.category_name = name
        self._price_modifier = price_modifier
        self.category_items = list()
        self._is_active = True
        return None

    def __str__(self):
        dict_to_json = {'category_id': self.category_id,
                        'category_name': self.category_name,
                        'category_items_qty': len(self.category_items),
                        'category._is_active': self._is_active}
        return str(dict_to_json)

    def add_category_item(self, item_style, item_name, item_size):
        item_idx = len(self.category_items)
        new_item = Item(self.category_id, item_idx, item_style, item_name,
                        item_size)
        self.category_items.append(new_item)
        return new_item

    def show_items(self):
        return self.category_items

    def update_category(self, category_id, name='', price_modifier=0):
        if name:
            self.category_name = name
        if price_modifier != 0:
            self._price_modifier = price_modifier
        dict_to_json = {'category_id': self.category_id,
                        'category_name': self.category_name,
                        'category_items_qty': len(self.category_items),
                        'category._is_active': self._is_active}
        return dict_to_json

    def remove_category_item(self, item_id):
        spam = self.category_items[item_id]
        del self.category_items[item_id]
        return spam

    @property
    def remove_category(self):
        self._is_active = False
        return self._is_active


class GoodItem(ABC):

    @abstractmethod
    def _get_fabric_price(self):
        pass

    @abstractmethod
    def _set_fabric_price(self):
        pass

    @abstractmethod
    def get_price(self):
        pass


class Item(GoodItem):
    item_list = list()

    def __init__(self, category_id, item_idx, item_style, item_name,
                 item_size):
        self.category_id = category_id
        self.item_idx = item_idx
        self.item_id = len(self.item_list)
        self.item_style = item_style
        self.item_name = item_name
        self.item_size = item_size
        self._fabric_price = self._get_fabric_price
        Item.item_list.append(self)
        return None

    def __str__(self):
        dict_to_json = {
            'category_id': self.category_id,
            'item_idx': self.item_idx,
            'item_id': self.item_id,
            'item_style': self.item_style,
            'item_name': self.item_name,
            'item_size': self.item_size,
            'item_price': self.get_price
        }
        return str(dict_to_json)

    @property
    def _get_fabric_price(self):
        self._fabric_price = randrange(2, 300)
        return self._fabric_price

    def _set_fabric_price(self):
        self._fabric_price = float(input('Введите закупочную стоимость: '))

    def update_item(self, item_id, item_style='', item_name='', item_size=''):
        if item_style:
            self.item_style = item_style
        if item_name:
            self.item_name = item_name
        if item_size:
            self.item_size = item_size
        dict_to_json = {
            'category_id': self.category_id,
            'item_id': self.item_id,
            'item_style': self.item_style,
            'item_name': self.item_name,
            'item_size': self.item_size,
            'item_price': self.get_price
        }
        return dict_to_json

    @property
    def remove_item(self):
        self._is_active = False
        return self._is_active

    @property
    def get_price(self):
        self.price = Catalog.currency_rate * self._fabric_price
        return self.price


class TestCatalog(unittest.TestCase):
    def setUp(self):
        self.category_id = 0
        self.category_name = 'Одежда'
        self.item_id = 1
        self.item_style = '1BLCNVYM'
        self.item_name = 'Куртка'
        self.item_size = 'M'
        self.tst_catalog = Catalog()

    def test_catalog(self):
        self.assertIsInstance(self.tst_catalog.currency_rate, float)
        self.assertIsInstance(self.tst_catalog.category_list, list)

    def test_catalog_str(self):
        tst_category = Category(self.category_id, 'test')
        Catalog.category_list.append(tst_category)
        self.assertIsInstance(str(self.tst_catalog.show_category(
            self.category_id)), str)


class TestCategory(unittest.TestCase):
    def setUp(self):
        self.category_id = 0
        self.category_name = 'Одежда'
        self.item_id = 0
        self.item_style = '1BLCNVYM'
        self.item_name = 'Куртка'
        self.item_size = 'M'
        self.tst_cat = Category(self.category_id, self.category_name)

    def test_category(self):
        cat_items_qty = len(self.tst_cat.category_items)
        self.assertIsInstance(str(self.tst_cat), str)

    def test_category_update(self):
        self.assertIsInstance(self.tst_cat.update_category(self.category_id,
                                                           'Обувь',
                                                           2.75), dict)

    def test_add_category_item(self):
        self.assertIsInstance(self.tst_cat.add_category_item(self.item_style,
                                                             self.item_name,
                                                             self.item_size),
                              Item)

    def test_remove_category_item(self):
        self.test_add_category_item()
        self.assertIsInstance(self.tst_cat.remove_category_item(self.item_id),
                              Item)

    def test_remove_category(self):
        self.assertFalse(self.tst_cat.remove_category)


class TestItem(unittest.TestCase):

    def setUp(self):
        self.category_id = 0
        self.item_idx = 0
        self.category_name = 'Одежда'
        self.item_id = 1
        self.item_style = '1BLCNVYM'
        self.item_name = 'Куртка'
        self.item_size = 'M'
        self.tst_item = Item(self.category_id, self.item_idx, self.item_style, self.item_name,
                             self.item_size)

    def test_item(self):
        self.assertIsInstance(str(self.tst_item), str)

    def test_update_item(self):
        self.assertIsInstance(self.tst_item.update_item(self.item_id,
                                                        '1WHTREDXL',
                                                        'Жилет', 'XL'), dict)

    def test_item_remove(self):
        self.assertFalse(self.tst_item.remove_item)


if __name__ == "__main__":
    unittest.main()
