from abc import ABC, abstractmethod
from random import randrange
import unittest


class Catalog:
    currency_rate = 0
    category_list = list()

    def __init__(self):
        Catalog.currency_rate = randrange(65, 80) * 0.99
        return None

    def __str__(self):
        return f'Курс доллара магазина: {self.currency_rate}'

    def show_category(cls, category_id):
        return cls.category_list[category_id]

    @property
    def fetch_currency_rate(self):
        self.currency_rate = randrange(65, 80)
        return self.currency_rate

    def show_all_categories(cls):
        print(cls.category_list)

    def search(self):
        pass


class Category:
    def __init__(self, category_id, name, price_modifier=1.0):
        self.category_id = category_id
        self.category_name = name
        self._price_modifier = price_modifier
        self.category_items = list()
        self._is_active = True

    def __str__(self):
        return (f'ID: {self.category_id}\nНазвание: {self.category_name}\n'
                f'Товаров: {len(self.category_items)}\n'
                f'Активна: {"Да" if self._is_active else "Нет"}\n')

    def add_category_item(self, item_style, item_name, item_size):
        new_item = Item(self.category_id, item_style, item_name, item_size)
        self.category_items.append(new_item)
        return new_item

    def show_items(self):
        return self.category_items

    def update_category(self, category_id, name='', price_modifier=0):
        if name:
            self.category_name = name
        if price_modifier != 0:
            self._price_modifier = price_modifier
        return (f'Категория изменена: {self.category_id} '
                f'{self.category_name} {self._price_modifier}'
                )

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

    def __init__(self, category_id, item_style, item_name, item_size):
        self.category_id = category_id
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

    def test_catalog(self):
        tst_catalog = Catalog()
        self.assertIsInstance(tst_catalog.currency_rate, float)
        self.assertIsInstance(tst_catalog.category_list, list)

        tst_category = Category(self.category_id, 'test')
        Catalog.category_list.append(tst_category)
        self.assertEqual(str(tst_catalog.show_category(self.category_id)),
                         (f'ID: {tst_category.category_id}\nНазвание: '
                          f'{tst_category.category_name}\nТоваров: '
                          f'{len(tst_category.category_items)}\nАктивна: '
                          f'{"Да" if tst_category._is_active else "Нет"}\n'))


class TestCategory(unittest.TestCase):
    def setUp(self):
        self.category_id = 0
        self.category_name = 'Одежда'
        self.item_id = 0
        self.item_style = '1BLCNVYM'
        self.item_name = 'Куртка'
        self.item_size = 'M'

    def test_category(self):
        tst_cat = Category(self.category_id, self.category_name)
        cat_items_qty = len(tst_cat.category_items)
        self.assertEqual(str(tst_cat), f'ID: {self.category_id}\n'
                         f'Название: {self.category_name}\n'
                         f'Товаров: {cat_items_qty}\n'
                         f'Активна: {"Да" if tst_cat._is_active else "Нет"}\n')

        self.assertEqual(tst_cat.update_category(self.category_id, 'Обувь',
                                                 2.75),
                         f'Категория изменена: {self.category_id} Обувь 2.75'
                         )

        self.assertIsInstance(tst_cat.add_category_item(self.item_style,
                                                        self.item_name,
                                                        self.item_size),
                              Item)

        self.assertIsInstance(tst_cat.remove_category_item(self.item_id),
                              Item)

        self.assertFalse(tst_cat.remove_category)


class TestItem(unittest.TestCase):

    def setUp(self):
        self.category_id = 0
        self.category_name = 'Одежда'
        self.item_id = 1
        self.item_style = '1BLCNVYM'
        self.item_name = 'Куртка'
        self.item_size = 'M'

    def test_item(self):
        tst_item = Item(self.category_id, self.item_style, self.item_name,
                        self.item_size)
        self.assertIsInstance(str(tst_item), str)

        self.assertIsInstance(tst_item.update_item(self.item_id, '1WHTREDXL',
                              'Жилет', 'XL'), dict)
        self.assertFalse(tst_item.remove_item)


if __name__ == "__main__":
    unittest.main()
