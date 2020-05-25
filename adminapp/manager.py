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

    @staticmethod
    def _create_category(name):
        category_id = len(Catalog.category_list)
        new_category = Category(category_id, name)
        Catalog.category_list.append(new_category)
        return new_category

    @staticmethod
    def _update_category(category_id, name, price_modifier):
        spam = Catalog.category_list[category_id].\
            update_category(category_id, name, price_modifier)
        return spam

    @staticmethod
    def _remove_category_item(item_id):
        category_id = Item.item_list[item_id].category_id
        item_idx = Item.item_list[item_id].item_idx
        del Catalog.category_list[category_id].category_items[item_idx]
        spam = Item.item_list[item_id].remove_item
        return spam

    @staticmethod
    def _remove_category(category_id):
        cat = Catalog.category_list[category_id]
        spam = type(cat), cat.remove_category
        del Catalog.category_list[category_id]
        return spam

    @staticmethod
    def _create_item(category_id, item_style, item_name, item_size):
        spam = Catalog.category_list[category_id].add_category_item(item_style,
                                                                    item_name,
                                                                    item_size
                                                                    )
        return spam

    @staticmethod
    def _update_item(item_id, item_style, item_name, item_size):
        spam = Item.item_list[item_id].update_item(item_style, item_name,
                                                   item_size)
        return spam

    @staticmethod
    def _remove_item(item_id):
        spam = Item.item_list[item_id].remove_item
        del Item.item_list[item_id]
        return spam


class TestManager(unittest.TestCase):
    def setUp(self):
        self.manager = Manager()
        self.category_id = 0
        self.category_name = 'Одежда'
        self.item_id = 0
        self.item_style = '1BLCNVYM'
        self.item_name = 'Куртка'
        self.item_size = 'M'
        self.tst_catalog = Catalog()
        self.tst_category = self.manager._create_category('test')

    def test_manager(self):
        self.assertIsInstance(self.manager, Manager)
        self.assertEqual(str(self.manager),
                         json.dumps({'id': self.manager.manager_id}))

    def test_create_category(self):
        self.assertIsInstance(self.tst_category, Category)
        self.assertEqual(len(self.tst_catalog.category_list), 1)

    def test_update_category(self):
        self.assertEqual(type(self.manager._update_category(self.category_id,
                                                            'Обувь',
                                                            2.78)), dict)

    def test_remove_category_item(self):
        self.test_create_item()
        self.assertFalse(self.manager._remove_category_item(self.item_id))

    def test_remove_category(self):
        self.assertEqual(self.manager._remove_category(self.category_id),
                         (Category, False))

    def test_create_item(self):
        self.assertIsInstance(self.manager._create_item(self.category_id,
                                                        self.item_style,
                                                        self.item_name,
                                                        self.item_size), Item)

    def test_update_item(self):
        self.assertIsInstance(self.manager._update_item(self.item_id,
                                                        '1REDXXL',
                                                        'Толстовка',
                                                        'XXL'), dict)

    def test_remove_item(self):
        self.test_create_item()
        self.assertFalse(self.manager._remove_item(self.item_id))


if __name__ == "__main__":
    unittest.main()
