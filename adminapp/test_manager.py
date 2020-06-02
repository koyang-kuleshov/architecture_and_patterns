import unittest
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

from adminapp import manager
from mainapp.catalog import Catalog, Category, Item


class TestManager(unittest.TestCase):
    def setUp(self):
        self.category_id = 0
        self.category_name = 'Одежда'
        self.item_id = 0
        self.item_style = '1BLCNVYM'
        self.item_name = 'Куртка'
        self.item_size = 'M'
        self.tst_catalog = Catalog()
        self.tst_category = manager._create_category('test')

    def test_create_category(self):
        self.assertIsInstance(self.tst_category, Category)
        self.assertIsInstance(self.tst_catalog.category_list, list)

    def test_update_category(self):
        self.assertEqual(type(manager._update_category(self.category_id,
                                                       'Обувь',
                                                       2.78)), dict)

    def test_remove_category_item(self):
        self.test_create_item()
        self.assertFalse(manager._remove_category_item(self.item_id))

    def test_remove_category(self):
        self.assertEqual(manager._remove_category(self.category_id),
                         (Category, False))

    def test_create_item(self):
        self.assertIsInstance(manager._create_item(self.category_id,
                                                   self.item_style,
                                                   self.item_name,
                                                   self.item_size), Item)

    def test_update_item(self):
        self.test_create_category()
        self.assertIsInstance(manager._update_item(self.item_id,
                                                   '1REDXXL',
                                                   'Толстовка',
                                                   'XXL'), dict)

    def test_remove_item(self):
        self.test_create_item()
        self.assertFalse(manager._remove_item(self.item_id))


if __name__ == "__main__":
    unittest.main()
