import unittest

from mainapp.catalog import Item
from mainapp.database import ItemSerializer


class TestItemSerializer(unittest.TestCase):

    def setUp(self):
        self.category_id = 0
        self.item_idx = 0
        self.category_name = 'Одежда'
        self.item_id = 1
        self.item_style = '1BLCNVYM'
        self.item_name = 'Куртка'
        self.item_size = 'M'
        self.tst_item = Item(self.category_id, self.item_idx, self.item_style,
                             self.item_name,
                             self.item_size)
        self.serializer = ItemSerializer()

    def test_item(self):
        result_json = self.serializer.serialize_items(self.tst_item)
        item = self.serializer.deserialize_items(result_json)
        self.assertIsInstance(item, Item)
        self.assertEqual(item.category_id, self.category_id)


if __name__ == "__main__":
    unittest.main()
