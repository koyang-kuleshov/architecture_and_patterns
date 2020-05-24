from random import randint
import unittest
import json

from mainapp.catalog import Catalog, Category, Item


class Manager:
    """Class for store manager"""

    def __init__(self):
        self.manager_id = randint(100, 1000)
        return None

    def __str__(self):
        return json.dumps({'id': self.manager_id})

    def _create_category(self, name):
        category_id = len(Catalog.category_list)
        new_category = Category(category_id, name)
        Catalog.category_list.append(new_category)
        return new_category

    def _update_category(self, category_id, name, price_modifier):
        Catalog.update_category(category_id, name, price_modifier)

    def _remove_category(self, category_id):
        cat = Catalog.category_list[category_id]
        spam = cat.remove_category()
        del Catalog.category_list[category_id]
        return (f'Категория {cat.category_id} {cat.category_name} удалена')

    def _create_item(self, category_id, item_style, item_name):
        Catalog.category_list[category_id].add_category_item(category_id,
                                                             item_style,
                                                             item_name
                                                             )

    def _update_item(self, item_id, item_style, item_name):
        Item[item_id].update_item(item_style, item_name)

    def _remove_item(self, item_id):
        Catalog.category_list[Item.item_list[item_id].category_id].\
            remove_category_item(item_id)
        del Item.item_list[item_id]
        self.category_list


class TestManager(unittest.TestCase):
    def setUp(self):
        self.manager = Manager()
        self.category_id = 0
        self.category_name = 'Одежда'
        self.category_new_name = 'Обувь'
        self.category_new_price = 2.99
        self.item_id = 1
        self.item_style = '1BLCNVYM'
        self.item_name = 'Куртка'
        self.item_size = 'M'

    def test_manager(self):
        self.assertIsInstance(self.manager, Manager)
        self.assertEqual(str(self.manager),
                         json.dumps({'id': self.manager.manager_id}))

    def test_create_category(self):
        tst_catalog = Catalog()
        tst_category = self.manager._create_category('test')
        self.assertIsInstance(tst_category, Category)
        self.assertEqual(len(tst_catalog.category_list), 1)


if __name__ == "__main__":
    unittest.main()
