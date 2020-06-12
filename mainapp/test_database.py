import unittest
import sqlite3
import os

from mainapp.catalog import Item
from mainapp.database import DatabaseMapper


class TestDatabaseMapper(unittest.TestCase):
    def setUp(self):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, 'patterns.sqlite')
        self.connection = sqlite3.connect(db_path)
        self.db_mapper = DatabaseMapper(self.connection)
        self.find_by_id = DatabaseMapper.find_by_id
        self.insert = DatabaseMapper.insert
        self.update = DatabaseMapper.update
        self.delete = DatabaseMapper.delete
        self.item = Item(0, 5, '4GRNWHTM', 'Рубашка', 'M')
        self.update_item = Item(0, 5, '4GRNWHTS', 'Рубашка', 'S')
        self.update_item.item_id = 5

    def test_find_by_id(self):
        self.assertIsInstance(self.find_by_id(self.db_mapper, 1), tuple)
        self.assertIsNone(self.find_by_id(self.db_mapper, 8))

    def test_insert(self):
        self.assertIsInstance(self.insert(self.db_mapper, self.item), int)

    def test_update(self):
        self.assertTrue(self.update(self.db_mapper, self.update_item))

    def test_delete(self):
        self.assertTrue(self.delete(self.db_mapper, self.update_item))


if __name__ == "__main__":
    unittest.main()
