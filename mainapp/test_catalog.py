import unittest
from mainapp.catalog import Catalog, Category, Item


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
        self.assertEqual(self.tst_catalog.currency_rate, {'_now': 70.0})
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

    def test_add_to_order(self):
        self.assertIsInstance(self.tst_item, Item)

    def test_update_item(self):
        self.assertIsInstance(self.tst_item.update_item(self.item_id,
                                                        '1WHTREDXL',
                                                        'Жилет', 'XL'), dict)

    def test_item_remove(self):
        self.assertFalse(self.tst_item.remove_item)


if __name__ == "__main__":
    unittest.main()
